from django.shortcuts import render
from django.http import JsonResponse
from .models import Product, ProductVariation
import pandas as pd
from django.conf import settings

def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'product_list.html', context)

def upload_products(request):
    if request.method == 'POST':
        file = request.FILES['file']
        if not file.name.endswith(('.xls', '.xlsx')):
            return JsonResponse({'error': 'Invalid file type'}, status=400)
        if file.size > 2 * 1024 * 1024:  # 2 MB
            return JsonResponse({'error': 'File size exceeds 2 MB'}, status=400)

        df = pd.read_excel(file)
        for _, row in df.iterrows():
            product_name = row['Product Name']
            variation_text = row['Variation']
            stock = row['Stock']

            product, created = Product.objects.get_or_create(product_name=product_name)
            if created:
                product.lowest_price = 0  # Default value or calculate based on your logic
                product.save()

            ProductVariation.objects.update_or_create(
                product=product,
                variation_text=variation_text,
                defaults={'stock': stock}
            )

        return JsonResponse({'message': 'File processed successfully'})
    return render(request, 'upload.html')
