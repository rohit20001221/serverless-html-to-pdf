import pdf from "html-pdf"

export default async function(req, res) {
    pdf.create("<h1>Hello World</h1>").toBuffer((err, buffer)=> {
        console.log(buffer)
        console.log(err)
        res.setHeader('Content-type','application/pdf')
        res.send(buffer)
    })
}