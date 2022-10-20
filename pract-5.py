# http node
# name - TestPage
# method - GET
# URL - /test

# function nade
# msg.payload=" Congratulations"
#return.msg;

# http responce node
# name test srvice
#  +add-select-Content-type-select text/html

# debug node
# deploy

# browser- localhost:1880/test

# back to function node
# write code
    var var1 = msg.req.query.var1
    var var2 = msg.req.query.var2
    msg.payload = parseInt(var1)+parseInt(var2)
    return msg;

# back to http node - Testpage
# URL- /add

# back to http responce node
# name - add service
# deploy

#browser Localhost:1880/add?var1=100&var2=30
# enter

