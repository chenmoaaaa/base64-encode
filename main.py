import base64
from os import path

if __name__ == "__main__":

    f_input = open('url.txt','r')
    data=f_input.read()

    f_input.close()

    output_encoded = base64.b64encode(data.encode("utf-8")).decode("utf-8")

    print("ecoded:",output_encoded)

    f_output = open(path.join('update','url'),'w')
    f_output.write(output_encoded)
    f_output.close()

    print("result saved.")