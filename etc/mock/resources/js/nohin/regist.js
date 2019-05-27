$(document).ready(function() {
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

	// animsition
	// $(".animsition").animsition();
	$(".animsition").animsition({
		inClass: 'fade-in',
		outClass: 'fade-out-up-sm',
		inDuration: 500,
		outDuration: 500,
		linkElement: '.animsition-link',
		// e.g. linkElement: 'a:not([target="_blank"]):not([href^="#"])'
		loading: true,
		loadingParentElement: 'body', //animsition wrapper element
		loadingClass: 'animsition-loading',
		loadingInner: '', // e.g '<img src="loading.svg" />'
		timeout: false,
		timeoutCountdown: 5000,
		onLoadEvent: true,
		browser: [ 'animation-duration', '-webkit-animation-duration'],
		// "browser" option allows you to disable the "animsition" in case the css property in the array is not supported by your browser.
		// The default setting is to disable the "animsition" in a browser that does not support "animation-duration".
		overlay : false,
		overlayClass : 'animsition-overlay-slide',
		overlayParentElement : 'body',
		// transition: execute(url)
		transition: function(url){
			if (url === void 0 || url == '') {
				return;
			} else {
				window.location.href = url;
			}
		}
	});

	// 納品先候補を作成
	createCompanyList();
	// 一覧部の商品選択候補を作成
	createShohinList();
	// 行追加ボタン押下時の処理
	$("#row_add_btn").on("click", addRow);
	// 行削除ボタン押下時の処理
	$(".js_row_delete_btn").on("click", deleteRow);

	// 商品選択時の処理
	$(".js_shohin").on("change", changeShohin);
	// 金額変更時の処理
	$(".js_price").on("input", changePrice);
	// 数量変更時の処理
	$(".js_amount").on("input", changeAmount);
});

var SEPARATOR = " ／ ";

/**
 * 納品先選択候補を作成
 */
function createCompanyList() {
	let modalCompanyList = $("#company_list");
	let optionList = [];
	let option;
	for (let company of companyJson) {
		option = $("<option>", { value: company.company_name });
		optionList.push(option);
	}
	modalCompanyList.append(optionList);
}

/**
 * 一覧部の商品選択候補を作成
 */
function createShohinList() {
	let modalShohinList = $("#shohin_list");
	let optionList = [];
	for (let shohin of shohinJson) {
		let content = shohin.kataban + SEPARATOR + shohin.shohin_name
		option = $("<option>", { value: content });
		optionList.push(option);
	}
	modalShohinList.append(optionList);
}

/**
 * 行追加ボタン押下時の処理
 */
function addRow() {
	$("#modal_table tbody tr:last-child").clone(true).appendTo("#modal_table tbody");
	$("#modal_table tbody tr:last-child input").val("");
	$("#modal_table tbody tr:last-child .zaikosu").text("");
}

/**
 * 行削除ボタン押下時の処理
 */
function deleteRow() {
	if($(".js_row_delete_btn").length != 1) {
		$(this).parent().parent().remove();
	}
	// 合計部の金額を設定する
	calcTotal();
}

/**
 * モーダルの商品選択時の処理
 */
function changeShohin() {
	let val = $(this).val();
	let kataban;
	let targetShohin = null;

	// 商品の型番を取得
	kataban = getKataban(val);
	// 型番に対応する商品情報（JSON）を取得
	targetShohin = getTargetShohinJson(kataban);

	if (targetShohin == null) {
		$(this).val("");
		$(this).closest("tr").find(".js_zaikosu").text("");
		return;
	}

	// 単価、在庫数に商品情報の値を設定する
	$(this).closest("tr").find(".js_price").val(targetShohin.price);
	$(this).closest("tr").find(".js_zaikosu").text(targetShohin.zaikosu.toLocaleString());
	// 合計部の金額を設定する
	calcTotal();
}

/**
 * 商品の型番を取得する
 */
function getKataban(val) {
	kataban = null;
	// 商品の型番を取得
	if (val.indexOf(SEPARATOR) == -1) {
		kataban = val;
	} else {
		kataban = val.substr(0, val.indexOf(SEPARATOR));
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
function calcTotal() {
	priceList = $(".js_price");
	amountList = $(".js_amount");
	let total = 0;
	let zeigaku = 0;
	let zeikomiTotal = 0;
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

	decimalTotal = new Decimal(total);
	zeiritsu = new Decimal(0.08);
	zeigaku = decimalTotal.times(zeiritsu).floor();
	zeikomiTotal = decimalTotal.plus(zeigaku);

	$(".js_zeinuki").text(decimalTotal.toNumber().toLocaleString());
	$(".js_shohizei").text(zeigaku.toNumber().toLocaleString());
	$(".js_zeikomi").text(zeikomiTotal.toNumber().toLocaleString());
}

/**
 * 数量変更時の処理
 */
function changeAmount() {
	calcTotal();
}

/**
 * 単価変更時の処理
 */
function changePrice() {
	calcTotal();
}
