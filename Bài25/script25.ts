let products: { name: string, price: number }[] = [
    { name: 'iphone13', price: 15000 },
    { name: 'iphone14', price: 18000 },
    { name: 'iphone15', price: 20000 },
]


// Vòng lặp For
for (let i = 0; i < products.length; i++) {
    if (products[i].price == 18000) {
        break;
    }
    console.log(products[i]);
}



let discount = 0;
let product = products[0];
switch (product.name) {
    case 'iphone13':
        discount = 5;
        break;

    case 'iphone14':
        discount = 10;
        break;


    case 'iphone15':
        discount = 15;
        break;

    default:
        discount = 100;
    // break;
}


console.log(`There is a ${discount}% on ${product.name}.`)