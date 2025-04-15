const express = require('express');
const axios = require('axios');
require("dotenv").config();

const router = express.Router();

router.get("/stock/:symbol", async (req, res) => {
      
    const {symbol} = req.params;

    try {

        const response = await axios.get(
         `https://data.alpaca.markets/v2/stocks/${symbol}/quotes/latest`  ,{
            headers: {
              "APCA-API-KEY-ID": process.env.ALPACA_KEY,
          "APCA-API-SECRET-KEY": process.env.ALPACA_SECRET,  
            }
         } 
        );
        const data = response.data;
        res.json(data);

        console.log(data);
        
    } catch (error) {
         res.status(500).json({ error: error.message });
    }
})