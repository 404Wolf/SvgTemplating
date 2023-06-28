from jinja2 import Environment, PackageLoader, select_autoescape
from gen.utils import fileAsBase64
from gen.renderer.render import renderPdf
from base64 import b64encode, b64decode


def main():
    jijnaEnv = Environment(
        loader=PackageLoader("gen", "templates"),
        autoescape=select_autoescape()
    )

    mySvg = jijnaEnv.get_template("example.svg")
    templated = mySvg.render(
        WORD="Propinquity",
        IMAGE=fileAsBase64("gen/wordImage.png"),
        PART_OF_SPEECH="noun",
        PART_OF_SPEECH_ICON=fileAsBase64("gen/nounIcon.svg"),
        PRONUNCIATION="proh-ping-kwuh-tee",
        INSPIRATIONAL_QUOTE="Propinquity breeds possibility; the closer we are to something, the more likely we are to achieve it",
        SYNONYM_1="Nearness",
        SYNONYM_2="Closeness",
        SYNONYM_3="Proximity",
        SYNONYM_4="Vicinity",
        SYNONYM_5="Contiguity",
        SYNONYM_6="Vicinage",
        SENTENCE_1="The <b>propinquity</b> of the two buildings made it easier to move equipment.",
        SENTENCE_2="The <b>propinquity</b> of the park to my house makes it my favorite spot.",
        SENTENCE_3="The <b>propinquity</b> of our workstations led to a friendship.",
    )

    rendered = renderPdf(
        data=b64encode(templated.encode("utf-8")).decode("utf-8"),
        mimetype="image/svg+xml",
        width=126,
        height=180
    )
    with open("output.pdf", "wb") as output:
        output.write(b64decode(rendered))

if __name__ == "__main__":
    main()
