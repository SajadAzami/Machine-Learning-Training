clear
load data.txt
rowCount = rows(data)
columnCount = columns(data)
x = data(1:rowCount)
lastIndex = columnCount*rowCount
y = data(rowCount+1:lastIndex)
plot(x,y,".")
xlabel('x')
ylabel('y')
title('Data Plot')