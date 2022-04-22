const express = require('express')
const app = express()

const {products} = require('./data')
const authorize = require('./authorize')

app.use(authorize)

app.get('/', (req, res)=>{
    const newProducts = products.map(product =>{
        const{name, desc, price} = product

        return {name, desc, price}
    })

    res.json(newProducts)

})

app.get('/api/:productID', (req, res)=>{
   const {productID} = req.params

   const singleProduct = products.find(product => product.id === Number(productID))
   
   if (!singleProduct) {
    return res.status(404).send('Product Does Not Exist')
  }


    res.json(singleProduct)

})

app.get('/query', (req, res)=>{
    

    res.send(req.query)

})




app.listen(5000, () => {
    console.log('Server is listening on port 5000....')
  })

