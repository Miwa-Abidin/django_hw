from shop.models import Item, Purchase

item1 = Item.objects.create(name='Mac', price=5000)

item1.purchases.create(name='Mirsaid Abidinov', age=25)
item1.purchases.create(name='Mirlan Abishef', age=23)

item2 = Item.objects.create(name='Windows', price=8000)

item2.purchases.create(name='Abubakr Mamatov', age=28)
item2.purchases.create(name='Mirlan Mamalaev', age=21)

item3 = Item.objects.create(name='Linux', price=6000)

item3.purchases.create(name='Arina Ten', age=17)
item3.purchases.create(name='Nurlan Karapkaev', age=28)

item4 = Item.objects.create(name='Televizor', price=12000)

item4.purchases.create(name='Aruuzhan Kazasheva', age=23)
item4.purchases.create(name='Alina Nazarbaeva', age=24)

item5 = Item.objects.create(name='Bicycle', price=9000)

item5.purchases.create(name='Myrza Alymbekov', age=25)
item5.purchases.create(name='Mirlan Aralashev', age=40)

item6 = Item.objects.create(name='Phone', price=15000)

item6.purchases.create(name='Nikita Verchuk', age=22)
item6.purchases.create(name='Aliya Omuralieva', age=19)

item7 = Item.objects.create(name='Car', price=50000)

item7.purchases.create(name='Uluk Abdilatov', age=36)
item7.purchases.create(name='Umut Bek', age=45)

item8 = Item.objects.create(name='Wheels', price=35000)

item8.purchases.create(name='Nurali Nurafenov', age=50)
item8.purchases.create(name='Nurafenali Nuragenov', age=53)

item9 = Item.objects.create(name='Computers', price=45000)

item9.purchases.create(name='Miwa Mishevich', age=29)
item9.purchases.create(name='Nurlan Mirlanov', age=23)

item10 = Item.objects.create(name='Tacos', price=1000)

item10.purchases.create(name='Mirbek Sirbekov', age=30)
item10.purchases.create(name='Ten Tenovich', age=25)

