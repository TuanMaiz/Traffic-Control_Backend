const mongoose = require('mongoose')

const resultSchema = new mongoose.Schema({ // làm theo hướng viết sẵn một số object sẽ được nhận, nếu ko xuất hiện thì là number = 0
    car: Number,
    person: Number,
    truck: Number,
    motorbike: Number,
    bus: Number,
    bicycle: Number,
})
const frameSchema = new mongoose.Schema({
    cameraID: {
        type: String,
        required: true,
    },
    frame: {}, //any
    date: {
        type: Date,
        required: true
    },
    result: resultSchema
})
module.exports = mongoose.model('Frame', frameSchema)