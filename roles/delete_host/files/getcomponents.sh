#Grepping the component names from the json content
grep -oP '(?<="component_name": ")[^"]*' /tmp/allclustercomponents.txt > /tmp/components.txt

