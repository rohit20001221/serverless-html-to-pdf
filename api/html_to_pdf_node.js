import pdf from "html-pdf"

export default async function(req, res) {
    pdf.create("<h1>Hello World</h1>").toBuffer(buffer => {
        res.setHeader('Content-type','application/pdf')
        res.send(buffer)
    })
}