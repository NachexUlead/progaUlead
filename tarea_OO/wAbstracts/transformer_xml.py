from  transformer import Transformer

class TransformerXML(Transformer):
    def serialize(self, obj):
        if not hasattr(obj, "__dict__"):
            raise ValueError("the object must have a __dict__ attribute")
        
        attributes = obj.__dict__
        xml = "<OBJECT>\n"

        for key, value in attributes.items():

            if key.startswith("_") and not key.startswith("__"):
                clean_key = key[1:]
                xml += f"<{clean_key}>{value}</{clean_key}>"
        
        xml += "</OBJECT>"
        return xml