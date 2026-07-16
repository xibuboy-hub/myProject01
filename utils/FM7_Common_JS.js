var datetime1 = new Date("2024/01/17 17:00:00");
var datetime2 = new Date("2024/01/17 17:00:00");
var nowdatetime = new Date();
var AccountID="(-:NewTypeFunc:Cookie('AccountID'):-)";

if ((Date.parse(datetime1) - Date.parse(nowdatetime) <= 0) && (Date.parse(datetime2) - Date.parse(nowdatetime) >= 0)) {
    window.location = "./construction.aspx";
}


var base64EncodeChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
var base64DecodeChars = new Array(
    -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
    -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
    -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 62, -1, -1, -1, 63,
    52, 53, 54, 55, 56, 57, 58, 59, 60, 61, -1, -1, -1, -1, -1, -1,
    -1,  0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14,
    15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, -1, -1, -1, -1, -1,
    -1, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
    41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, -1, -1, -1, -1, -1);

function base64encode(str) {
    var out, i, len;
    var c1, c2, c3;

    len = str.length;
    i = 0;
    out = "";
    while(i < len) {
	c1 = str.charCodeAt(i++) & 0xff;
	if(i == len)
	{
	    out += base64EncodeChars.charAt(c1 >> 2);
	    out += base64EncodeChars.charAt((c1 & 0x3) << 4);
	    out += "==";
	    break;
	}
	c2 = str.charCodeAt(i++);
	if(i == len)
	{
	    out += base64EncodeChars.charAt(c1 >> 2);
	    out += base64EncodeChars.charAt(((c1 & 0x3)<< 4) | ((c2 & 0xF0) >> 4));
	    out += base64EncodeChars.charAt((c2 & 0xF) << 2);
	    out += "=";
	    break;
	}
	c3 = str.charCodeAt(i++);
	out += base64EncodeChars.charAt(c1 >> 2);
	out += base64EncodeChars.charAt(((c1 & 0x3)<< 4) | ((c2 & 0xF0) >> 4));
	out += base64EncodeChars.charAt(((c2 & 0xF) << 2) | ((c3 & 0xC0) >>6));
	out += base64EncodeChars.charAt(c3 & 0x3F);
    }
    return out;
}

function base64decode(str) {
    var c1, c2, c3, c4;
    var i, len, out;

    len = str.length;
    i = 0;
    out = "";
    while(i < len) {
	/* c1 */
	do {
	    c1 = base64DecodeChars[str.charCodeAt(i++) & 0xff];
	} while(i < len && c1 == -1);
	if(c1 == -1)
	    break;

	/* c2 */
	do {
	    c2 = base64DecodeChars[str.charCodeAt(i++) & 0xff];
	} while(i < len && c2 == -1);
	if(c2 == -1)
	    break;

	out += String.fromCharCode((c1 << 2) | ((c2 & 0x30) >> 4));

	/* c3 */
	do {
	    c3 = str.charCodeAt(i++) & 0xff;
	    if(c3 == 61)
		return out;
	    c3 = base64DecodeChars[c3];
	} while(i < len && c3 == -1);
	if(c3 == -1)
	    break;

	out += String.fromCharCode(((c2 & 0XF) << 4) | ((c3 & 0x3C) >> 2));

	/* c4 */
	do {
	    c4 = str.charCodeAt(i++) & 0xff;
	    if(c4 == 61)
		return out;
	    c4 = base64DecodeChars[c4];
	} while(i < len && c4 == -1);
	if(c4 == -1)
	    break;
	out += String.fromCharCode(((c3 & 0x03) << 6) | c4);
    }
    return out;
}


function JSRedirect(pages,para,anchor)
{
	para=base64encode(para);
	if(typeof(anchor) == 'undefined') 
		location.replace(pages+"?EinB64="+para);
	else
		location.replace(pages+"?EinB64="+para+"#"+anchor);		
}

function JSOpenWin(pages,para,attrs,names)
{
	para=base64encode(para);
	window.open(pages+"?EinB64="+para,names,attrs);
}

function AccChoose(Type,FormName,IDItem,NameItem,DIDItem,DNameItem,Comp)
{
	URLS="FM7_AccDeptChoose_Win.aspx?Type="+Type+"&FormName="+FormName+"&Comp="+Comp;
	
	if(IDItem != "") URLS=URLS+"&IDItem="+IDItem;
	if(NameItem != "") URLS=URLS+"&NameItem="+NameItem;
	if(DIDItem != "") URLS=URLS+"&DIDItem="+DIDItem;
	if(DNameItem != "") URLS=URLS+"&DNameItem="+DNameItem;
	
	AccWin=window.open(URLS,"AccMWin", "top=100,left=400,scrollbars=yes,location=no,directories=no,width=500,height=500");
	AccWin.focus();
}

function SelectDepts(FormName,DIDItem,DNameItem,Types)
{

	var DeptIDList=eval("document."+FormName+"."+DIDItem);
	DeptIDList=DeptIDList.value;
	var DeptNameList=eval("document."+FormName+"."+DNameItem);
	DeptNameList=DeptNameList.value;
	var DURLS="FM7_SelectDepts_Win.aspx?FormName="+FormName;
	DURLS=DURLS+"&DIDItem="+DIDItem;
	DURLS=DURLS+"&DNameItem="+DNameItem;
	DURLS=DURLS+"&Types="+Types;
	DURLS=DURLS+"&DeptIDList="+DeptIDList;
	DURLS=DURLS+"&DeptNameList="+DeptNameList;
	SelectDWin=window.open(DURLS,"SelectDWin", "top=20,left=400,scrollbars=yes,location=no,directories=no,width=600,height=650");
	SelectDWin.focus();
}

function SelectMems(FormName,IDItem,NameItem,Types)
{
	var AccountIDList=eval("document."+FormName+"."+IDItem);
	AccountIDList=AccountIDList.value;
	var NameList=eval("document."+FormName+"."+NameItem);
	NameList=NameList.value;
	var URLS="FM7_SelectMembers_Win.aspx?FormName="+FormName;
	URLS=URLS+"&IDItem="+IDItem;
	URLS=URLS+"&NameItem="+NameItem;
	URLS=URLS+"&Types="+Types;
	URLS=URLS+"&AccountIDList="+AccountIDList;
	URLS=URLS+"&NameList="+NameList;
	
	SelectWin=window.open(URLS,"SelectWin", "top=20,left=400,scrollbars=yes,location=no,directories=no,width=600,height=650");
	SelectWin.focus();
}
