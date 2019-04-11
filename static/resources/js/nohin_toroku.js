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

	// モーダルの納品先候補を作成
	createModalCompanyList();
	// モーダルの一覧部の商品選択候補を作成
	createModalShohinList();
	// 画面右下の登録ボタン押下時の処理
	$(".js_regist_btn").on("click", showRegistModal);
	// 各行の更新ボタン押下時の処理
	$(".js_update_btn").on("click", showUpdateModal);
	// ------------------------------
	// 登録用モーダルの処理
	// TODO:画面を分割
	// ------------------------------
	/*
	// TODO:この処理の作成は後にまわす
	// 行追加ボタン押下時の処理
	$("#row_add_btn").on("click", modalAddRow);
	// 行削除ボタン押下時の処理
	$(".js_row_delete_btn").on("click", modalDeleteRow);
	*/
	// 商品選択時の処理
	$(".js_modal_shohin").on("change", modalChangeShohin);
	// 金額変更時の処理
	$(".js_modal_price").on("input", modalChangePrice);
	// 数量変更時の処理
	$(".js_modal_amount").on("input", modalChangeAmount);
	// ------------------------------
	// 更新用モーダルの処理
	// TODO:画面を分割
	// ------------------------------
	// 商品選択時の処理
	$(".js_update_modal_shohin").on("change", updateModalChangeShohin);
	// 金額変更時の処理
	$(".js_update_modal_price").on("input", updateModalChangePrice);
	// 数量変更時の処理
	$(".js_update_modal_amount").on("input", updateModalChangeAmount);

	// モーダルを開くか判別
	if (openRegistModal == 'True') {
		$('#regist_nohin_modal').modal();
		calcTotal($(".js_total"));
	}
});

//---------------------------------------
// 以下、納品情報登録用モーダル用の処理
//---------------------------------------
/**
 * 画面右下の登録ボタン押下時の処理
 */
function showRegistModal() {
	$('#regist_nohin_modal').modal();
}

/**
 * モーダルの行追加ボタン押下時の処理
 */
function modalAddRow() {
	$("#modal_table tbody tr:last-child").clone(true).appendTo("#modal_table tbody");
	$("#modal_table tbody tr:last-child input").val("");
	$("#modal_table tbody tr:last-child .zaikosu").text("");
}

/**
 * モーダルの行削除ボタン押下時の処理
 */
function modalDeleteRow() {
	if($(".js_row_delete_btn").length != 1) {
		$(this).parent().parent().remove();
	}
}

/**
 * モーダルの商品選択時の処理
 */
function modalChangeShohin() {
	let val = $(this).val();
	let kataban ;
	let targetShohin = null;

	// 商品の型番を取得
	kataban = getKataban(val);
	// 型番に対応する商品情報（JSON）を取得
	targetShohin = getTargetShohinJson(kataban);

	if (targetShohin == null) {
		$(this).val("");
		$(this).closest("tr").find(".zaikosu").text("");
		return;
	}

	// 単価、在庫数に商品情報の値を設定する
	$(this).closest("tr").find(".js_modal_price").val(targetShohin.price);
	$(this).closest("tr").find(".zaikosu").text(targetShohin.zaikosu.toLocaleString());
	total = calcTotal($(".js_modal_price"), $(".js_modal_amount"));
	$(".js_total").text(total.toLocaleString());
}

/**
 * モーダルの単価変更時の処理
 */
function modalChangePrice() {
	total = calcTotal($(".js_modal_price"), $(".js_modal_amount"));
	$(".js_total").text(total.toLocaleString());
}

/**
 * モーダルの数量変更時の処理
 */
function modalChangeAmount() {
	total = calcTotal($(".js_modal_price"), $(".js_modal_amount"));
	$(".js_total").text(total.toLocaleString());
}

//---------------------------------------
// 以下、納品情報更新用モーダル用の処理
//---------------------------------------
/**
 * 各行の更新ボタン押下時の処理
 */
function showUpdateModal() {
	clearUpdateModal();
	$('#update_nohin_date').val($(this).data('nohin_date'));
	$('#update_nohinsaki').val($(this).data('nohinsaki'));
	$('#update_memo').val($(this).data('memo'));

	let nohinDetailList = nohinDetailJson[$(this).data('nohin_id')]
	let detail;
	for (let i = 0; i < nohinDetailList.length; i++) {
		detail = nohinDetailList[i];
		$("#update_nohin_modal").find("#id_form-" + i +"-kataban").val(detail.kataban);
		$("#update_nohin_modal").find("#id_form-" + i +"-price").val(detail.price);
		let amount = $("#update_nohin_modal").find("#id_form-" + i +"-amount")
		amount.val(detail.amount);

		noSlashKataban = getKataban(detail.kataban);
		targetShohin = getTargetShohinJson(noSlashKataban);
		// 在庫数に商品情報の値を設定する
		amount.closest("tr").find(".zaikosu").text(targetShohin.zaikosu.toLocaleString());
	}

	// 合計金額を計算
	total = calcTotal($(".js_update_modal_price"), $(".js_update_modal_amount"));
	$(".js_update_total").text(total.toLocaleString());

	$('#update_nohin_modal').modal();
}

/**
 * 更新用モーダルをクリアする
 */
function clearUpdateModal() {
	$('#update_nohin_date').val("");
	$('#update_nohinsaki').val("");
	$('#update_memo').val("");
	$(".js_update_modal_shohin").val("");
	$(".js_update_modal_price").val("");
	$(".js_update_modal_amount").val("");
	$("#update_nohin_modal").find(".zaikosu").text("");
	$(".js_update_total").text("");
}

/**
 * モーダルの商品選択時の処理
 */
function updateModalChangeShohin() {
	let val = $(this).val();
	let kataban ;
	let targetShohin = null;

	// 商品の型番を取得
	kataban = getKataban(val);
	// 型番に対応する商品情報（JSON）を取得
	targetShohin = getTargetShohinJson(kataban);

	if (targetShohin == null) {
		$(this).val("");
		$(this).closest("tr").find(".zaikosu").text("");
		return;
	}

	// 単価、在庫数に商品情報の値を設定する
	$(this).closest("tr").find(".js_update_modal_price").val(targetShohin.price);
	$(this).closest("tr").find(".zaikosu").text(targetShohin.zaikosu.toLocaleString());
	total = calcTotal($(".js_update_modal_price"), $(".js_update_modal_amount"));
	$(".js_update_total").text(total.toLocaleString());
}

/**
 * モーダルの単価変更時の処理
 */
function updateModalChangePrice() {
	total = calcTotal($(".js_update_modal_price"), $(".js_update_modal_amount"));
	$(".js_update_total").text(total.toLocaleString());
}

/**
 * モーダルの数量変更時の処理
 */
function updateModalChangeAmount() {
	total = calcTotal($(".js_update_modal_price"), $(".js_update_modal_amount"));
	$(".js_update_total").text(total.toLocaleString());
}

//--------------------------------------------
// 以下、納品情報登録用、更新用モーダル共通の処理
//--------------------------------------------
/**
 * モーダルの納品先選択候補を作成
 */
function createModalCompanyList() {
	let modalCompanyList = $("#modal_company_list");
	let optionList = [];
	let option;
	for (let company of companyJson) {
		option = $("<option>", { value: company.company_name });
		optionList.push(option);
	}
	modalCompanyList.append(optionList);
}

/**
 * モーダルの一覧部の商品選択候補を作成
 */
function createModalShohinList() {
	let modalShohinList = $("#modal_shohin_list");
	let optionList = [];
	for (let shohin of shohinJson) {
		let content = shohin.kataban + " ／ " + shohin.shohin_name
		option = $("<option>", { value: content });
		optionList.push(option);
	}
	modalShohinList.append(optionList);
}

/**
 * 商品の型番を取得する
 */
function getKataban(val) {
	kataban = null;
	// 商品の型番を取得
	if (val.indexOf("／") == -1) {
		kataban = val.trim();
	} else {
		kataban = val.substr(0, val.indexOf("／")).trim();
	}
	return kataban;
}

/**
 * 型番に対応する商品情報（JSON）を取得する
 */
function getTargetShohinJson(kataban) {
	targetShohin = null;
	// 型番に対応する商品情報（JSON）を取得
	for (let shohin of shohinJson) {
		if (shohin.kataban == kataban) {
			targetShohin = shohin;
			break;
		}
	}
	return targetShohin;
}

/**
 * 合計金額を計算する
 */
// function calcTotal(target) {
function calcTotal(priceList, amountList) {
	let total = 0;
	let price;
	let amount;

	for (let i = 0; i < priceList.length; i++) {
		price = priceList[i].valueAsNumber;
		amount = amountList[i].valueAsNumber;
		if (Number.isNaN(price) || Number.isNaN(amount)) {
			continue;
		}
		total += price * amount;
	}

	return total;
}
