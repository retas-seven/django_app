var tmpRow;

$(function(){
	// wow
	new WOW().init();
	
	// easeScroll
	$("html").easeScroll({
		frameRate: 60,
		animationTime: 1000,
		stepSize: 120,
		pulseAlgorithm: 1,
		pulseScale: 8,
		pulseNormalize: 1,
		accelerationDelta: 20,
		accelerationMax: 1,
		keyboardSupport: true,
		arrowScroll: 50,
		touchpadSupport: true,
		fixedBackground: true
	});

	// モーダルの行追加ボタン押下時の処理
	$("#row_add_btn").on("click", registModalAddRow);
	// モーダルの行削除ボタン押下時の処理
	$(".js_row_delete_btn").on("click", registModalDeleteRow);
	// モーダルの商品選択時の処理
	$("[name=registShohin]").on("change", registModalChangeShohin);
});

/**
 * モーダルの行追加ボタン押下時の処理
 */
function registModalAddRow() {
	$("#modal_table tbody tr:last-child").clone(true).appendTo("#modal_table tbody");
	$("#modal_table tbody tr:last-child input").val("");
}

/**
 * モーダルの行削除ボタン押下時の処理
 */
function registModalDeleteRow() {
	if($(".js_row_delete_btn").length != 1) {
		$(this).parent().parent().remove();
	}
}

/**
 * モーダルの商品選択時の処理
 */
function registModalChangeShohin() {
}
