import pdf from "html-pdf"
import path from "path"

export default async function (req, res) {
    pdf.create("<h1>hello world</h1>", {
        phantomPath: path.resolve(
            process.cwd(),
            "node_modules/phantomjs-prebuilt/lib/phantom/bin/phantomjs"
        ),
    }).toBuffer((err, buffer) => {
        console.log(buffer)
        console.log(err)
        res.setHeader('Content-type', 'application/pdf')
        res.send(buffer)
    })
}