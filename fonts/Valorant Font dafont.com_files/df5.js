var itext=0;function textoff(elt){if(itext==0) elt.value="";itext=1;}function themesoff(){var elt1=document.getElementById("themes1");var elt2=document.getElementById("themes2");if(document.body.clientWidth<880) {if(elt1) elt1.style.display="none";if(elt2) elt2.style.display="none";}else{if(elt1) elt1.style.display="block";if(elt2) elt2.style.display="block";}}function bgadoff(){document.getElementById("ad1").style.background="url(http://www.dafont.com/img/hello1.gif) no-repeat";document.getElementById("ad2").style.background="url(http://www.dafont.com/img/hello2.gif) no-repeat"}function change_pselect(current,last){if(document.getElementById){var elt=document.getElementById(current);elt.style.display="inline";var elt2=document.getElementById(last);elt2.style.display="none";}}function change_block(current,last){if(document.getElementById){var elt=document.getElementById(current);elt.style.display="block";var elt2=document.getElementById(last);elt2.style.display="none";}}function checkl(c,tab){if(c.checked==true){v=tab.split('|');for(i=0;i<v.length;i++){document.getElementById(v[i]).checked=true;}}}var ht=window.innerHeight;

/*
// Chrome
function scrollpos(){if(document.getElementById("ad2")){scroll1=document.documentElement.scrollTop?document.documentElement.scrollTop:document.body.scrollTop;var sky=document.getElementById("sky");var ad2=document.getElementById("ad2");if(scroll1>"165"){if(document.getElementById("sky")){sky.style.position="fixed";sky.style.top="18px";ad2.style.position="fixed";ad2.style.top="18px"}}else{	if(document.getElementById("sky")){sky.style.position="absolute";sky.style.top="183px";ad2.style.position="absolute";ad2.style.top="183px"}}}}var ht=document.documentElement.clientHeight;
*/

// FF
function scrollpos(){if(document.getElementById("ad2")){scroll1=document.documentElement.scrollTop?document.documentElement.scrollTop:document.body.scrollTop;var sky=document.getElementById("sky");var ad2=document.getElementById("ad2");if(scroll1>"168"){if(document.getElementById("sky")){sky.style.top="18px";ad2.style.top="18px"}}else{if(document.getElementById("sky")){sky.style.top=183-scroll1+"px";ad2.style.top=183-scroll1+"px";}}}}var ht=window.innerHeight;