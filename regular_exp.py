import re

input_string = "Dict(keys=[Constant(value='Brand'), Constant(value='Source'), Constant(value='Native_Product_Id'), Constant(value='Subcategory1'), Constant(value='Subcategory2'), Constant(value='Subcategory3'), Constant(value='Native_Subcategory'), Constant(value='Title'), Constant(value='Display_Title'), Constant(value='Original_Price'), Constant(value='Selling_Price'), Constant(value='Discount_Percentage'), Constant(value='Description'), Constant(value='Item_Url'), Constant(value='Display_Image'), Constant(value='Primary_Colour'), Constant(value='Image_Urls'), Constant(value='Size'), Constant(value='product_detail')], values=[Constant(value='Aurelia'), Constant(value='Aurelia'), Subscript(value=Name(id='i', ctx=Load()), slice=Constant(value='sku'), ctx=Load()), Subscript(value=Attribute(value=Name(id='response', ctx=Load()), attr='meta', ctx=Load()), slice=Constant(value='subcat1'), ctx=Load()), Subscript(value=Attribute(value=Name(id='response', ctx=Load()), attr='meta', ctx=Load()), slice=Constant(value='subcat2'), ctx=Load()), Name(id='subcategory3', ctx=Load()), Name(id='native_subcategory', ctx=Load()), Subscript(value=Name(id='i', ctx=Load()), slice=Constant(value='name'), ctx=Load()), Subscript(value=Name(id='i', ctx=Load()), slice=Constant(value='name'), ctx=Load()), Subscript(value=Name(id='i', ctx=Load()), slice=Constant(value='price'), ctx=Load()), Subscript(value=Name(id='i', ctx=Load()), slice=Constant(value='selling_price'), ctx=Load()), Subscript(value=Name(id='i', ctx=Load()), slice=Constant(value='discount'), ctx=Load()), Subscript(value=Name(id='i', ctx=Load()), slice=Constant(value='description'), ctx=Load()), BinOp(left=BinOp(left=Constant(value='https://shopforaurelia.com/'), op=Add(), right=Subscript(value=Name(id='i', ctx=Load()), slice=Constant(value='url_key'), ctx=Load())), op=Add(), right=Constant(value='.html')), Subscript(value=Name(id='i', ctx=Load()), slice=Constant(value='image'), ctx=Load()), Subscript(value=Name(id='i', ctx=Load()), slice=Constant(value='color'), ctx=Load()), Name(id='images', ctx=Load()), Name(id='size', ctx=Load()), Call(func=Attribute(value=Name(id='json', ctx=Load()), attr='dumps', ctx=Load()), args=[Name(id='product_detail', ctx=Load())], keywords=[])])"

# Define a regular expression pattern to match all 'id' and 'attr' values


# Apply the regular expression to the input string using findall

def findre(s):
    pattern = r"Name\(id='([^']+)',\s*ctx=Load\(\)\)|attr='([^']+)'"
    matches = re.findall(pattern, input_string)
    matches = [value for match in matches for value in match if value]
    return matches
# Flatten the list of tuples and remove empty strings
matches = findre(input_string)

# Extract and print all matched values
if matches:
    for i, match in enumerate(matches, start=1):
        print(f"{i}. {match}")
else:
    print("No matches found.")

