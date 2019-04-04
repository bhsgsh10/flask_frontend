#http://127.0.0.1:5000/

from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

currentId = 31
fruits = [{
    "Id": 1,
    "Name": "Apple",
    "Season": "All year",
    "Price_$": "2.00",
    "Vitamin_A": "Available",
    "Vitamin_C": "Available",
    "ImageUrl": "https://images.pexels.com/photos/102104/pexels-photo-102104.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500",
    "Description": "An apple is a sweet, edible fruit produced by an apple tree (Malus pumila). Apple trees are cultivated worldwide and are the most widely grown species in the genus Malus. The tree originated in Central Asia, where its wild ancestor, Malus sieversii, is still found today. Apples have been grown for thousands of years in Asia and Europe and were brought to North America by European colonists. Apples have religious and mythological significance in many cultures, including Norse, Greek and European Christian traditions."
},
{
    "Id": 2,
    "Name": "Banana",
    "Season": "All year",
    "Price_$": "3.00",
    "Vitamin_A": "Available",
    "Vitamin_C": "Not available",
    "ImageUrl": "https://i5.walmartimages.ca/images/Large/580/6_r/875806_R.jpg",
    "Description": "Bananas are one of the most widely consumed fruits in the world for good reason. Eating them could help lower blood pressure and reduce the risks of cancer and asthma."
},
{
    "Id": 3,
    "Name": "Star fruit",
    "Season": "All year",
    "Price_$": "10.00",
    "Vitamin_A": "Not available",
    "Vitamin_C": "Available",
    "ImageUrl": "https://i0.wp.com/images.mapsofindia.com/my-india/2017/02/2_Carambola.jpg?ssl=1",
    "Description": "This fruit with a waxy skin makes a great preserve or pickle. While the unripe ones are green in colour and sour to taste, the ripened ones have a distinctly yellow colour, with slightly brown ribs are sweet. The fruit is grown throughout India, but especially in the Southern parts"
},
{
    "Id": 4,
    "Name": "Mangosteen",
    "Season": "All year",
    "Price_$": "10.00",
    "Vitamin_A": "Not available",
    "Vitamin_C": "Available",
    "ImageUrl": "https://i2.wp.com/images.mapsofindia.com/my-india/2017/02/5_Mangosteen.jpg?ssl=1",
    "Description": "This tropical fruit is fragrant and the leathery purple-maroon shell surrounds a moist, snow-white and sweet fleshy interior. The flavour of the fruit is mellow and earthy, and is similar to mango in taste. Mangosteen is the national fruit of Thailand. They flourish in the Southern parts of India"
},
{
    "Id": 5,
    "Name": "Phalsa",
    "Season": "Summer",
    "Price_$": "7.00",
    "Vitamin_A": "Not available",
    "Vitamin_C": "Available",
    "ImageUrl": "https://i2.wp.com/images.mapsofindia.com/my-india/2017/02/10_Phalsa.jpg?ssl=1",
    "Description": "Phalsa fruit is a perfect blend between sweet and sour flavours. This super fruit has effective cooling properties and when ripe, can be eaten with a sprinkling of salt and black pepper. The fruit is also used in making syrups and squashes. It is grown throughout India."
},
{
    "Id": 6,
    "Name": "Mango",
    "Season": "Summer",
    "Price_$": "12.00",
    "Vitamin_A": "Not available",
    "Vitamin_C": "Available",
    "ImageUrl": "https://upload.wikimedia.org/wikipedia/commons/7/79/Alphonso_mango.jpg",
    "Description": "Mangoes are juicy stone fruit (drupe) from numerous species of tropical trees belonging to the flowering plant genus Mangifera, cultivated mostly for their edible fruit. The majority of these species are found in nature as wild mangoes. The genus belongs to the cashew family Anacardiaceae. Mangoes are native to South Asia."
},
{
    "Id": 7,
    "Name": "Strawberry",
    "Season": "All year",
    "Price_$": "12.00",
    "Vitamin_A": "Not available",
    "Vitamin_C": "Available",
    "ImageUrl": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/PerfectStrawberry.jpg/440px-PerfectStrawberry.jpg",
    "Description": "The garden strawberry (or simply strawberry) is a widely grown hybrid species of the genus Fragaria, collectively known as the strawberries. It is cultivated worldwide for its fruit. The fruit is widely appreciated for its characteristic aroma, bright red color, juicy texture, and sweetness. It is consumed in large quantities, either fresh or in such prepared foods as preserves, juice, pies, ice creams, milkshakes, and chocolates."
},
{
    "Id": 8,
    "Name": "Orange",
    "Season": "Summer",
    "Price_$": "5.00",
    "Vitamin_A": "Not available",
    "Vitamin_C": "Available",
    "ImageUrl": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Single_Orange_%28Fruit%29.jpg/440px-Single_Orange_%28Fruit%29.jpg",
    "Description": "The orange is the fruit of the citrus species Citrus sinensis in the family Rutaceae. It is also called sweet orange, to distinguish it from the related Citrus aurantium, referred to as bitter orange. The sweet orange reproduces asexually (apomixis through nucellar embryony) varieties of sweet orange arise through mutations."
},
{
    "Id": 9,
    "Name": "Pineapple",
    "Season": "All year",
    "Price_$": "8.00",
    "Vitamin_A": "Not available",
    "Vitamin_C": "Available",
    "ImageUrl": "https://images-na.ssl-images-amazon.com/images/I/71%2BqAJehpkL._SY355_.jpg",
    "Description": "The pineapple (Ananas comosus) is a tropical plant with an edible multiple fruit consisting of coalesced berries, also called pineapples, In 2016, Costa Rica, Brazil, and the Philippines accounted for nearly one-third of the world's production of pineapples."
},
{
    "Id": 10,
    "Name": "Grape",
    "Season": "All year",
    "Price_$": "8.00",
    "Vitamin_A": "Not available",
    "Vitamin_C": "Available",
    "ImageUrl": "https://upload.wikimedia.org/wikipedia/commons/b/bb/Table_grapes_on_white.jpg",
    "Description": "A grape is a fruit, botanically a berry, of the deciduous woody vines of the flowering plant genus Vitis. Grapes can be eaten fresh as table grapes or they can be used for making wine, jam, juice, jelly, grape seed extract, raisins, vinegar, and grape seed oil. Grapes are a non-climacteric type of fruit, generally occurring in clusters."
},
{
    "Id": 11,
    "Name": "Jambolan",
    "Season": "Summer",
    "Price_$": "8.00",
    "Vitamin_A": "Not available",
    "Vitamin_C": "Available",
    "ImageUrl": "https://nurserylive.com/images/stories/virtuemart/product/eugenia-jamibolana-jamun.jpg",
    "Description": "Syzygium cumini, commonly known as jambolan, Java plum, black plum or jamun, is an evergreen tropical tree in the flowering plant family Myrtaceae. It is native to the Indian Subcontinent, adjoining regions of Southeast Asia, China and Queensland.[1] The name of the fruit is sometimes mistranslated as blackberry, which is a different fruit in an unrelated order. Syzygium cumini has been spread overseas from India by Indian emigrants and at present is common in former tropical British colonies."
},
{
    "Id": 12,
    "Name": "Pear",
    "Season": "All year",
    "Price_$": "8.00",
    "Vitamin_A": "Not available",
    "Vitamin_C": "Available",
    "ImageUrl": "https://i.ebayimg.com/images/g/R6QAAOSwAvJXAnrq/s-l300.jpg",
    "Description": "The pear tree and shrub are a species of genus Pyrus, in the family Rosaceae, bearing the pomaceous fruit of the same name. Several species of pear are valued for their edible fruit and juices while others are cultivated as trees."
},
{
    "Id": 13,
    "Name": "Papaya",
    "Season": "Summer",
    "Price_$": "13.00",
    "Vitamin_A": "Available",
    "Vitamin_C": "Available",
    "ImageUrl": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Papaya_cross_section_BNC.jpg/1599px-Papaya_cross_section_BNC.jpg",
    "Description": "The papaya is a small, sparsely branched tree, usually with a single stem growing from 5 to 10 m tall, with spirally arranged leaves confined to the top of the trunk."
},
{
    "Id": 14,
    "Name": "Jackfruit",
    "Season": "Summer",
    "Price_$": "8.00",
    "Vitamin_A": "Not available",
    "Vitamin_C": "Available",
    "ImageUrl": "https://previews.123rf.com/images/dole/dole1502/dole150200001/37053275-ripe-jackfruit-jack-fruit-isolated-on-white-background.jpg",
    "Description": "The jackfruit tree is well-suited to tropical lowlands, and its fruit is the largest tree-borne fruit, reaching as much as 55 kg (120 lb) in weight, 90 cm (35 in) in length, and 50 cm (20 in) in diameter. A mature jackfruit tree can produce about 100 to 200 fruits in a year. The jackfruit is a multiple fruit, composed of hundreds to thousands of individual flowers, and the fleshy petals are eaten."
},
{
    "Id": 15,
    "Name": "Clementine",
    "Season": "Summer",
    "Price_$": "10.00",
    "Vitamin_A": "Not available",
    "Vitamin_C": "Available",
    "ImageUrl": "https://upload.wikimedia.org/wikipedia/commons/6/62/Clementine_del_golfo_di_Taranto_IGP.jpg",
    "Description": "A clementine (Citrus clementina) is a tangor, a hybrid between a willowleaf mandarin orange (C. deliciosa) and a sweet orange (C. sinensis), so named in 1902. y appearance."
},
{
    "Id": 16,
    "Name": "Acai",
    "Season": "Winter",
    "Price_$": "15.00",
    "Vitamin_A": "Not available",
    "Vitamin_C": "Available",
    "ImageUrl": "https://usercontent1.hubstatic.com/14145580_f520.jpg",
    "Description": "If you go to Brazil, you will notice that acai is absolutely everywhere. There are cafes and shops dedicated to the fruit selling anything from acai ice cream to fruit bowls to even towels and hoodies with acai printed on them. As with everything, there are some people who love acai and others do not care much for it. "
},
{
    "Id": 17,
    "Name": "Lime",
    "Season": "Summer",
    "Price_$": "10.00",
    "Vitamin_A": "Not available",
    "Vitamin_C": "Available",
    "ImageUrl": "https://image.shutterstock.com/image-photo/ripe-wedge-green-lime-citrus-260nw-618439478.jpg",
    "Description": "A lime is a citrus fruit, which is typically round, green in color, 3 to 6 centimetres in diameter, and contains acidic juice vesicles."
},
{
    "Id": 18,
    "Name": "Watermelon",
    "Season": "Summer",
    "Price_$": "10.00",
    "Vitamin_A": "Available",
    "Vitamin_C": "Available",
    "ImageUrl": "https://thumbs.dreamstime.com/z/watermelon-slices-wooden-table-55476817.jpg",
    "Description": "The watermelon is an annual that has a prostrate or climbing habit. Stems are up to 3 m long and new growth has yellow or brown hairs. Leaves are 60 to 200 mm long and 40 to 150 mm wide. These usually have three lobes which are themselves lobed or doubly lobed. Plants have both male and female flowers on 40-mm-long hairy stalks. These are yellow, and greenish on the back."
},
{
    "Id": 19,
    "Name": "Fig",
    "Season": "Summer",
    "Price_$": "10.00",
    "Vitamin_A": "Available",
    "Vitamin_C": "Available",
    "ImageUrl": "https://img1.southernliving.timeinc.net/sites/default/files/styles/4_3_horizontal_inbody_900x506/public/image/2016/01/main/2121201_figs022_sdw.jpg?itok=k-B7qd15",
    "Description": "Ficus carica is an Asian species of flowering plant in the mulberry family, known as the common fig (or just the fig). It is the source of the fruit also called the fig and as such is an important crop in those areas where it is grown commercially. Native to the Middle East and western Asia, it has been sought out and cultivated since ancient times and is now widely grown throughout the world, both for its fruit and as an ornamental plant. The species has become naturalized in scattered locations in Asia and North America"
},
{
    "Id": 20,
    "Name": "Avocado",
    "Season": "All year",
    "Price_$": "10.00",
    "Vitamin_A": "Available",
    "Vitamin_C": "Available",
    "ImageUrl": "https://static.independent.co.uk/s3fs-public/thumbnails/image/2019/03/24/14/avocados.jpg?w968h681",
    "Description": "These fruits have a smooth and delicious texture and flavor that makes them great on sandwiches and in salads, blended into sauces and dressings, and can even be used as an alternative to butter and oil to add healthy fat and flavor to things like pudding and cake."
},
{
    "Id": 21,
    "Name": "Dragon fruit",
    "Season": "All year",
    "Price_$": "10.00",
    "Vitamin_A": "Available",
    "Vitamin_C": "Available",
    "ImageUrl": "https://i1.wp.com/youshouldgrow.com/wp-content/uploads/Dragon-Fruit.jpg?zoom=2&resize=526%2C335&ssl=1",
    "Description": "Dragon fruit is also used in smoothies, salad dressing, homemade wines, and as an additive in sauces. Depending on the variety of dragon fruit, the flesh may also be white. Both have a mild but satisfying sweetness and a smooth texture accented by a slight crunch from the tiny black seeds within it."
},
{
    "Id": 22,
    "Name": "Finger limes",
    "Season": "All year",
    "Price_$": "10.00",
    "Vitamin_A": "Available",
    "Vitamin_C": "Available",
    "ImageUrl": "https://cdn3.volusion.com/hreny.ypnsh/v/vspfiles/photos/FINGERLIME12-2.jpg?1519345394",
    "Description": "Also referred to as the caviar of limes, these finger shaped limes have a green oily skin that is very fragrant. Previously only grown in Australia, this exotic fruit has only recently been grown in the United States."
},
{
    "Id": 23,
    "Name": "Passion fruit",
    "Season": "All year",
    "Price_$": "10.00",
    "Vitamin_A": "Available",
    "Vitamin_C": "Available",
    "ImageUrl": "https://www.attainable-sustainable.net/wp-content/uploads/2011/08/passion-fruit-jelly-480x270.jpg",
    "Description": "There are many types of passion fruit ranging in color from purple to yellow. Depending on the variety, it will grow in zones 6-11. The fruit produces very crunchy seeds within sacs of sweet and tart juice. They are easy to grow, but be careful!"
},
{
    "Id": 24,
    "Name": "Meyer lemon",
    "Season": "All year",
    "Price_$": "10.00",
    "Vitamin_A": "Available",
    "Vitamin_C": "Available",
    "ImageUrl": "https://www.gourmetsleuth.com/images/default-source/dictionary/meyerlemon-jpg.jpg?sfvrsn=4",
    "Description": "The darling of chefs, the Meyer lemon is a favorite exotic fruit of the citrus clan. It is sweeter and less tart than a traditional lemon and is therefore favored for use in desserts and drinks like lemonade and cocktails. The rind is also favored for flavoring in cooking"
},
{
    "Id": 25,
    "Name": "Guava",
    "Season": "Summer",
    "Price_$": "10.00",
    "Vitamin_A": "Available",
    "Vitamin_C": "Available",
    "ImageUrl": "https://usercontent2.hubstatic.com/14145585_f520.jpg",
    "Description": "Nearly nonexistent in the Northern Hemisphere, guavas are extremely abundant in Brazil. Fresh guavas are the most popular, but there are also juices and sweets, such as the goiabada. Goiabada can be referred to as the guava variation of canned cranberry sauce due to its color and texture."
},
{
    "Id": 26,
    "Name": "Champagne orange",
    "Season": "All year",
    "Price_$": "7.00",
    "Vitamin_A": "Not available",
    "Vitamin_C": "Available",
    "ImageUrl": "https://usercontent1.hubstatic.com/14145566.jpg",
    "Description": "If you search this title in Google, a number of drink recipes involving mixing champagne and oranges will show up. Champagne taste can greatly be enhanced by adding orange juice and the resulting creation is often referred to as a mimosa."
},
{
    "Id": 27,
    "Name": "Jabuticaba",
    "Season": "All year",
    "Price_$": "7.00",
    "Vitamin_A": "Not available",
    "Vitamin_C": "Available",
    "ImageUrl": "https://usercontent2.hubstatic.com/14145573_f520.jpg",
    "Description": "This fruit can be described as a darker version of a blueberry, although it is much larger. A jabuticaba is around the size of a plum and these fruits grow straight on tree trunks. All parts of the fruit are edible, although the sweet flesh is much more pleasing to taste buds than the sour skin. Jabuticaba is a superfruit that is abundant in Brazil, however, for some reason, we cannot seem to find it in the produce section of US supermarkets. The explanation for that is that this delicious fruit is highly perishable. The giant berries are only good for a few short days after being harvested. Are you burning with the desire to taste this fruit that is bursting with antioxidants? Although there are rumors about jabuticaba being imported to Japan and sold there, you will get the most out of your experience by visiting Brazil, the country this detox fruit is indigenous to."
},
{
    "Id": 28,
    "Name": "Cupuacu",
    "Season": "All year",
    "Price_$": "9.00",
    "Vitamin_A": "Not available",
    "Vitamin_C": "Available",
    "ImageUrl": "https://usercontent2.hubstatic.com/14145605.jpg",
    "Description": "Cupuacu is a very strange-looking fruit. These fruits look like huge kiwis on the outside and tend to weigh around 1 kilogram each. Cupuacu has a white-colored pulp with a seed pod in the center, whose scent can be described as that of pineapple and chocolate at the same time. And some say that it smells like a banana. But do not let that scare you."
},
{
    "Id": 29,
    "Name": "Guarana",
    "Season": "All year",
    "Price_$": "9.00",
    "Vitamin_A": "Not available",
    "Vitamin_C": "Available",
    "ImageUrl": "https://usercontent1.hubstatic.com/14145608_f520.jpg",
    "Description": "Guarana Antarctica is Brazil\'s traditional non alcoholic drink. Soft drinks typically are not associated with fruits, so what is the case with this one? Gurana also happens to be the name of a Brazilian fruit, whose seeds contain more than twice as much caffeine as coffee seeds. Guarana is used in the production of this popular Brazilian soda and has been used as a key Brazilian soft drink ingredient since 1909."
},
{
    "Id": 30,
    "Name": "Cashew apple",
    "Season": "All year",
    "Price_$": "15.00",
    "Vitamin_A": "Not available",
    "Vitamin_C": "Available",
    "ImageUrl": "https://usercontent2.hubstatic.com/14145613.jpg",
    "Description": "The caju, or cashew when translated from Portuguese, is a fairly common and affordable nut in North America. "
},
{
    "Id": 31,
    "Name": "Siriguela",
    "Season": "All year",
    "Price_$": "15.00",
    "Vitamin_A": "Not available",
    "Vitamin_C": "Available",
    "ImageUrl": "https://usercontent1.hubstatic.com/14145614_f520.jpg",
    "Description": "The name siriguela is just as exotic as the fruit itself. This small round fruit is native to northeastern Brazil, where it is extremely popular. Siriguelas are eaten with their skin on; their small size makes it impractical to attempt to remove the skin prior to consumption. This yellowish fruit tastes and looks like a miniature mango and is very juicy. Brazilians like to enjoy siriguela on its own as a snack and some use it in juices or to flavor ice creams. "
},
{
    "Id": 32,
    "Name": "Cagaita",
    "Season": "All year",
    "Price_$": "15.00",
    "Vitamin_A": "Not available",
    "Vitamin_C": "Available",
    "ImageUrl": "https://usercontent1.hubstatic.com/14145616_f520.jpg",
    "Description": "The cagaita is a Brazilian superfruit, unknown to the outside world. It is worth mentioning that it is not only the fruit itself that gets used. The leaves, bark and fruits have medicinal properties and locals use the tree wood for construction and charcoal. Cagaita fruits themselves either get eaten as they are or get used to make ice cream, juices, and even liqueurs. The leaves and bark of the cagaita tree are believed to be able to help those suffering from diabetes."
}
]

@app.route('/save_item', methods=['GET', 'POST'])
def save_item():
    global fruits
    global currentId
    json_data = request.get_json()
    name = json_data['Name']
    season = json_data['Season']
    price = json_data['Price_$']
    vitaminA = json_data['Vitamin_A']
    vitaminC = json_data['Vitamin_C']
    imageUrl = json_data['ImageUrl']
    description = json_data['Description']
    currentId += 1
    new_id = currentId
    new_fruit = {
        "Id": new_id,
        "Name": name,
        "Season": season,
        "Price_$": price,
        "Vitamin_A": vitaminA,
        "Vitamin_C": vitaminC,
        "ImageUrl": imageUrl,
        "Description": description
    }
    fruits.append(new_fruit)

    return jsonify(new_id=new_id)


# @app.route('/save_sale', methods=['GET', 'POST'])
# def save_sale():
#     global sales
#     global clients
#     global current_id
#     json_data = request.get_json()
#     print(json_data)
#     salesperson = json_data['salesperson']
#     client = json_data['client']
#     reams = json_data['reams']
#     current_id += 1
#     new_id = current_id
#     new_sale_entry = {
#         "id": new_id,
#         "salesperson": salesperson,
#         "client": client,
#         "reams": reams
#     }
#     if client not in clients:
#         clients.append(client)

#     sales.append(new_sale_entry)
#     return jsonify(sales = sales, clients = clients)


@app.route('/addItem')
def addItem(name=None):
    return render_template('addItem.html', fruits=fruits)

@app.route('/search')
def search(name=None):
    return render_template('search.html', fruits=fruits)

@app.route('/item/<item_id>')
def item(item_id=None):
    return render_template('item.html', item_id=item_id, fruits=fruits)

if __name__ == '__main__':
   app.run(debug = True)

