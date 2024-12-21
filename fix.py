def choose_product(category):
    if category not in products:
        print("❌ ไม่มีสินค้าในหมวดหมู่นี้ ❌")
        return

    category_products = products[category]
    print(f"\n🎯 --- รายการสินค้าในหมวด {category.upper()} --- 🎯")
    for index, (product_name, details) in enumerate(category_products.items(), start=1):
        print(f"\n✨ {index}. {details['description']} ✨")
        print(f"   💵 ราคา: {details['price_per_rate']:.2f} บาท ต่อ {details['min_quantity']} ชิ้น")
        print(f"   📦 จำนวนขั้นต่ำ: {details['min_quantity']} ชิ้น")
        print(f"   📦 จำนวนสูงสุด: {details['max_quantity']} ชิ้น")
        if 'example_link' in details:
            print(f"   🔗 ตัวอย่างลิงก์: {details['example_link']}")

    print("\n🔙 0. ย้อนกลับ")

    try:
        choice = int(input("\n🔔 กรุณาเลือกสินค้าที่ต้องการ: "))
        if choice == 0:
            return  # ย้อนกลับไปยังเมนูหลัก
        elif 1 <= choice <= len(category_products):
            selected_product = list(category_products.items())[choice - 1]
            product_name, product_details = selected_product
            print(f"\nคุณเลือกสินค้า: {product_details['description']}")
            quantity = int(input(f"กรุณากรอกจำนวนที่ต้องการ (ขั้นต่ำ {product_details['min_quantity']} และสูงสุด {product_details['max_quantity']}): "))
            if quantity < product_details['min_quantity'] or quantity > product_details['max_quantity']:
                print(f"❌ จำนวนสินค้าต้องอยู่ระหว่าง {product_details['min_quantity']} ถึง {product_details['max_quantity']} ชิ้น ❌")
            else:
                link = input("กรุณากรอกลิงก์ที่ต้องการ: ")
                place_order(category, product_name, quantity, link)
        else:
            print("❌ กรุณาเลือกสินค้าจากตัวเลือกที่ถูกต้อง ❌")
    except ValueError:
        print("❌ กรุณากรอกตัวเลขที่ถูกต้อง ❌")