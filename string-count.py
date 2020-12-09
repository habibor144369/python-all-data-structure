# string counting row python----
string = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore ' \
         'magna aliqua. Lectus vestibulum mattis ullamcorper velit sed ullamcorper morbi tincidunt. Sapien faucibus et ' \
         'molestie ac feugiat sed. Amet est placerat in egestas erat imperdiet sed. Sodales ut eu sem integer vitae justo' \
         ' eget. Quam id leo in vitae turpis massa sed. Suspendisse in est ante in nibh. Semper risus in hendrerit gravida ' \
         'rutrum quisque. Quis varius quam quisque id diam vel quam elementum. Tortor dignissim convallis aenean et. Sed cras' \
         ' ornare arcu dui vivamus arcu felis bibendum ut. Nisi porta lorem mollis aliquam ut porttitor leo. Eget mi proin sed ' \
         'libero enim sed. Convallis a cras semper auctor neque vitae tempus. Viverra adipiscing at in tellus integer feugiat. ' \
         'Odio tempor orci dapibus ultrices. Turpis egestas integer eget aliquet nibh. Tincidunt id aliquet risus feugiat. Vitae ' \
         'tempus quam pellentesque nec nam aliquam sem. Eu lobortis elementum nibh tellus molestie.'
count = 0
for i in string:
    result = i.count(i)
    count += result  # count = count + result
print(count)
