multipleClick_clickTime = null; multipleClick_target = null; function preventMultipleClick(id) { sameTarget = false; if(id==multipleClick_target) { sameTarget = true; } multipleClick_target = id; fastClick = false; var currentClickTime = new Date(); if (currentClickTime - multipleClick_clickTime < 1500) {fastClick = true;} multipleClick_clickTime = currentClickTime; return (sameTarget && fastClick); }
var current_item = null; var current_timeout = null; 
function display(id){
    new_menu = $( id );
    if (current_item == null) {
        current_item = new_menu;
        new_menu.fadeIn(); 
    } else if (current_item == new_menu) {
        return; 
    } else {
        current_item.stop( true, true ).fadeOut(complete=function() { 
            current_item = new_menu; 
            new_menu.fadeIn();
        });
    }
}

var listBarcodes = {}
function insertBarcode(barcode) { 
    console.log("New barcode read: ", barcode);
    if (barcode in listBarcodes) {
        listBarcodes[barcode] = listBarcodes[barcode] + 1;
        $('#'+barcode).parent().stop(true, true).toggleClass("highlight").delay(300).queue(function() { $('#'+barcode).text(listBarcodes[barcode]); $('#'+barcode).parent().stop(true, true).toggleClass("highlight");});;
    } else {
        listBarcodes[barcode] = 1;
        $('#productsList').append('<li class="list-group-item"><span class="badge" id="'+barcode+'"></span><img src="barcode-icon.png"/> '+barcode+'</li>');
        $('#'+barcode).parent().stop(true, true).toggleClass("highlight").delay(300).queue(function() { $('#'+barcode).text(listBarcodes[barcode]); $('#'+barcode).parent().stop(true, true).toggleClass("highlight");});;
    }
}

var subscriberName = "barcode-reader-webpage";
var theContext;
var theVideoDevice;
var theLastImage = [];



var currentProductImage="1";
var newProductImage="2";
function toggleProductImages() {
    if (currentProductImage=="1") {
        currentProductImage="2";
        newProductImage="1";
    } else {
        currentProductImage="1";
        newProductImage="2";
    }
    $("#product-image-"+newProductImage).fadeOut("slow", function() { $("#product-image-"+currentProductImage).fadeIn("slow"); });
    
}