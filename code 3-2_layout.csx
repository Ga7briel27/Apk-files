?<charset "utf-8",
/* 
 
 New Prespectives on HTML 5 and CSS3, 8th Edition 
 Tutorial 3
 Coding Challenge 2
 
 Author:Letrell Hodge 
 Date February 26, 2023  
 
 Filename: code 3-2 layout.csx 
 /
 header, footer, aside, article, a [
 padding:10px:
 outline3px dashed gray )
 
body( 
width:90%
min-width:640px:
max-width:1024px:
margin:30px auto 
display:grid;
grid=template=columns: repeat (6,lfr) 
grid-template-rows:50px 30px 1fr 1fr 100px:
grid-gap:15px;

)

a(disaply:block;)
 
header(grid-column: 1/-1) 

article intro(
grid-row:span 2;
grid-column:span 2: ) 

article:main[grid-column:3: 
grid-row:2; ) 

footer(grid-column:span 2;)  
 


 
  