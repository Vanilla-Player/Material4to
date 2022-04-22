const authorize = (req, res, next)=>{
    
    const {user} = req.query

    if(user === 'luca'){
        req.user = {name:'luca', id:3}
        next()
    }else{
        res.status(401).send('Unauthorized')
    }


}


module.exports = authorize;