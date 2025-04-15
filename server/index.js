const cors = require('cors')
const express = require('express')
const app = express()
const stockRouter = require("./stock")

app.use(cors());
app.use(express.json());
app.use("/api", stockRouter);

app.get('/', (req , res) => {
    res.send("API gawk")

});

app.listen(5000 , () => {
    console.log("Server is running on port 5000")
})