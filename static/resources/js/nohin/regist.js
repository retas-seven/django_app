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

	// 画面の初期表示状態を設定
	init();
	// 納品先候補を作成
	createCompanyList();
	// 一覧部の商品選択候補を作成
	createShohinList();

	// 行追加ボタン押下時の処理
	$("#row_add_btn").on("click", addRow);
	// 行削除ボタン押下時の処理
	$(".js_row_delete_btn").on("click", deleteRow);
	// 行トグルボタン押下時の処理
	$(".js_row_toggle_btn").on("click", toggleRow);

	// 商品選択時の処理
	$(".js_shohin").on("change", changeShohin);
	// 金額変更時の処理
	$(".js_price").on("input", changePrice);
	// 数量変更時の処理
	$(".js_amount").on("input", changeAmount);

	// 登録／更新ボタン押下時の処理
	$(".js_execute_btn").on("click", execute);
});

var SEPARATOR = " ／ ";

/**
 * 画面初期化
 */
function init() {
	let form = $('[name=nohin_form]');

	// TODO: 更新画面で、行を削除状態にしてsubmitした際、
	// 入力チェックエラーなどで戻り遷移しすると、
	// 見た目が通常行と同じになってしまうことの暫定対処として、
	// 削除チェックボックスのチェックを外す。
	$('[id^="id_form"][id$="-DELETE"]').prop("checked", false);

	if (mode == 'regist') {
		form.attr('action', nohinRegistViewUrl);
		
	} else if (mode == 'update') {
		form.attr('action', nohinUpdateViewUrl);
		// 既存行の合計金額を設定する
		calcTotal();
	}
};

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
	// $("#detail_table tbody tr:last-child").clone(true).appendTo("#detail_table tbody");
	// $("#detail_table tbody tr:last-child input").val("");
	// $("#detail_table tbody tr:last-child .zaikosu").text("");
	
	// 新規行を追加
	let formIdx = $('#id_form-TOTAL_FORMS').val();
	let newRow = $(".js_empty_row tbody tr:last-child").clone(true);
	newRow.appendTo("#detail_table tbody");

	// 新規行に追加する入力項目を作成
	let emptyKataban = $('#id_form-__prefix__-kataban');
	let emptyPrice = $('#id_form-__prefix__-price');
	let emptyAmount = $('#id_form-__prefix__-amount');
	let newRowKataban = emptyKataban[0].outerHTML.replace(/__prefix__/g, formIdx);
	let newRowPrice = emptyPrice[0].outerHTML.replace(/__prefix__/g, formIdx);
	let newRowAmount= emptyAmount[0].outerHTML.replace(/__prefix__/g, formIdx);

	// 新規行に入力項目を設定
	$("#detail_table tbody tr:last-child .js_dummy_kataban").replaceWith(newRowKataban);
	$("#detail_table tbody tr:last-child .js_dummy_price").replaceWith(newRowPrice);
	$("#detail_table tbody tr:last-child .js_dummy_amount").replaceWith(newRowAmount);

	// 新規行に追加した入力項目を取得し、入力時のイベントを設定
	newRowKatabanElement = $('#id_form-' + formIdx + '-kataban');
	newRowPriceElement = $('#id_form-' + formIdx + '-price');
	newRowAmountElement = $('#id_form-' + formIdx + '-amount');
	newRowKatabanElement.on("change", changeShohin);
	newRowPriceElement.on("input", changePrice);
	newRowAmountElement.on("input", changeAmount);

	// let formIdx = $('#id_form-TOTAL_FORMS').val();
	// $("#detail_table tbody").append($('.js_empty_row').html().replace(/__prefix__/g, formIdx));
	$('#id_form-TOTAL_FORMS').val(parseInt(formIdx) + 1);
}

/**
 * 行削除ボタン押下時の処理
 */
function deleteRow() {
	// if($(".js_row_delete_btn").length != 1) {
	// 	$(this).parent().parent().remove();
	// }
	$(this).parent().parent().remove();
	
	// 合計部の金額を設定する
	calcTotal();
}

/**
 * 行トグルボタン押下時の処理
 */
function toggleRow() {
	delCheckbox = $(this).siblings('input[type="checkbox"]');
	currentRow = $(this).parent().parent();

	if (delCheckbox.prop("checked")) {
		// 行を有効化する
		delCheckbox.prop("checked", false);
		currentRow.removeClass('js_deleted_row');
		currentRow.find(':input').attr('readonly', false);
		$(this).html('<i class="fas fa-times"></i>')
	} else {
		// 行を無効化する
		delCheckbox.prop("checked", true);
		currentRow.addClass('js_deleted_row');
		currentRow.find('input').attr('readonly', true);
		$(this).html('<i class="fas fa-undo"></i>')
	}
	
	// 合計部の金額を設定する
	calcTotal();
}

/**
 * 商品選択時の処理
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
		$(this).closest("tr").find(".js_price").val("");
		$(this).closest("tr").find(".js_amount").val("");

		// 合計部の金額を設定する
		calcTotal();
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
		// 読取専用（＝更新画面で、削除状態にされた行）は計算対象外
		if(priceList[i].readOnly && amountList[i].readOnly) {
			continue;
		}

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

/**
 * 登録／更新ボタン押下時の処理
 */
function execute() {
	$('body').on('animsition.outEnd', () => {
		let form = $('[name=nohin_form]');
		form.submit();
	});
};
