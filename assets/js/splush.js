var BASE = 'http://www.feedasplush.com';

if (typeof SPLUSH_KEY == 'undefined' || SPLUSH_KEY == '')
  SPLUSH_KEY = 'error';
if (typeof SPLUSH_IMAGE == 'undefined' || SPLUSH_IMAGE == '')
  SPLUSH_IMAGE = 1;
if (typeof SPLUSH_FORMAT == 'undefined' || SPLUSH_FORMAT == '')
  SPLUSH_FORMAT = 1;
if (typeof SPLUSH_DATE == 'undefined' || SPLUSH_DATE == '')
  SPLUSH_FORMAT = 1;
if (typeof SPLUSH_BCOLOR == 'undefined' || SPLUSH_BCOLOR == '')
  SPLUSH_BCOLOR = 'ffffff';
if (typeof SPLUSH_LCOLOR == 'undefined' || SPLUSH_LCOLOR == '')
  SPLUSH_LCOLOR = '000000';
if (typeof SPLUSH_TCOLOR == 'undefined' || SPLUSH_TCOLOR == '')
  SPLUSH_TCOLOR = '000000';
if (typeof SPLUSH_ICOLOR == 'undefined' || SPLUSH_ICOLOR == '')
  SPLUSH_ICOLOR = '000000';
if (typeof SPLUSH_WIDTH == 'undefined' || SPLUSH_WIDTH < 160)
  SPLUSH_WIDTH = 160;
if (typeof SPLUSH_WTHEME == 'undefined' || SPLUSH_WTHEME == '')
  SPLUSH_WHTEME = 'light';

var THEME = '/bcolor/' + SPLUSH_BCOLOR
             + '/lcolor/' + SPLUSH_LCOLOR
             + '/tcolor/' + SPLUSH_TCOLOR
             + '/icolor/' + SPLUSH_ICOLOR
             + '/width/' + SPLUSH_WIDTH
             + '/wtheme/' + SPLUSH_WTHEME;
             
var URL = BASE + '/feeds/widget/view/key/' + SPLUSH_KEY + '/page/1' + '/format/' + SPLUSH_FORMAT + '/date/' + SPLUSH_DATE + '/image/' + SPLUSH_IMAGE + THEME;
var HEIGHT = 373;
HEIGHT += 3;
document.write('<iframe style="border:none;padding:0;margin:0;width:' + SPLUSH_WIDTH + 'px;height:' + HEIGHT + 'px;" src="' + URL + '" frameborder="0"></iframe>');
