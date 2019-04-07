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
	// モーダルの行追加ボタン押下時の処理
	$("#row_add_btn").on("click", modalAddRow);
	// モーダルの行削除ボタン押下時の処理
	$(".js_row_delete_btn").on("click", modalDeleteRow);
	// モーダルの商品選択時の処理
	$(".js_modal_shohin").on("change", modalChangeShohin);
	// モーダルの商品選択時の処理
	$(".js_modal_price").on("input", modalChangePrice);
	// モーダルの商品選択時の処理
	$(".js_modal_amount").on("input", modalChangeAmount);

	// モーダルを開くか判別
	if (openRegistModal == 'True') {
		$('#regist_nohin_modal').modal();
		calcTotal($(".js_total"));
	}
});

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
	if (val.indexOf("／") == -1) {
		kataban = val.trim();
	} else {
		kataban = val.substr(0, val.indexOf("／")).trim();
	}

	// 型番に対応する商品情報（JSON）を取得
	for (let shohin of shohinJson) {
		if (shohin.kataban == kataban) {
			targetShohin = shohin;
			break;
		}
	}

	if (targetShohin == null) {
		$(this).val("");
		$(this).closest("tr").find(".zaikosu").text("");
		return;
	}

	// 単価、在庫数に商品情報の値を設定する
	$(this).closest("tr").find(".js_modal_price").val(targetShohin.price);
	$(this).closest("tr").find(".zaikosu").text(targetShohin.zaikosu.toLocaleString());
	calcTotal($(".js_total"));
}

/**
 * モーダルの単価変更時の処理
 */
function modalChangePrice() {
	calcTotal($(".js_total"));
}

/**
 * モーダルの数量変更時の処理
 */
function modalChangeAmount() {
	calcTotal($(".js_total"));
}

/**
 * 合計金額を計算する
 */
function calcTotal(target) {
	let priceList = $(".js_modal_price");
	let amountList = $(".js_modal_amount");
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

	target.text(total.toLocaleString());
}