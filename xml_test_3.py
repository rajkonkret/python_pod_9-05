from xml.dom import minidom

root = minidom.Document()
xml = root.createElement('root')
root.appendChild(xml)

productChild = root.createElement('product')
productChild.setAttribute('name', 'Geek')

xml.appendChild(productChild)

xml_str = root.toprettyxml(indent='\t')
save_path = 'gfg.xml'
with open(save_path, 'w') as f:
    f.write(xml_str)