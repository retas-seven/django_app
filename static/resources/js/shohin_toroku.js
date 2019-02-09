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

	// 商品登録モーダルを開くか判別
	if ($('.js_open_dialog').val() == "True") {
		$('.js_btn_update').addClass('is_hide');
		$('#shohin_toroku_modal').modal();
	}

	/**
	 * 削除ボタン押下時の処理
	 */
    $('.js_delete_btn').click(function(e) {
        if(!confirm('削除しますか？')){
            return false;
        }
		
		kataban = $(this).parents('td').data('kataban');
		form = $('[name=shohins_sakujo_form]');
		$('.js_shohin_sakujo_key_kataban').val(kataban);
		form.submit();
	});
	
	/**
	 * ダイアログ（登録）表示ボタン押下時の処理
	 */
    $('.js_toroku_btn').click(function(e) {
		$('#id_kataban').val('');
		$('#id_shohinName').val('');
		$('#id_price').val('');
		$('#id_zaikosu').val('');
		$('#id_memo').val('');
		
		$('#id_kataban').attr('readonly', false);
		$('#id_kataban').removeClass('form-control-plaintext');

		// 更新、登録ボタンの表示切り替え
		$('.js_btn_update').addClass('is_hide');
		$('.js_btn_regist').removeClass('is_hide');

		// formのアクション設定
		form = $('[name=shohins_toroku_form]');
		form.attr('action', getShohinTorokuUrl());

		$('#shohin_toroku_modal').modal();
	});
	
	/**
	 * ダイアログ（更新）表示ボタン押下時の処理
	 */
    $('.js_koshin_btn').click(function(e) {
		let datas = $(this).parents('td');

		$('#id_kataban').val(datas.data('kataban'));
		$('#id_shohinName').val(datas.data('shohin_name'));
		$('#id_price').val(datas.data('price'));
		$('#id_zaikosu').val(datas.data('zaikosu'));
		$('#id_memo').val(datas.data('memo'));
		
		// 型番は読み取りのみとし、更新させない
		$('#id_kataban').attr('readonly', true);
		$('#id_kataban').addClass('form-control-plaintext');

		// 更新、登録ボタンの表示切り替え
		$('.js_btn_regist').addClass('is_hide');
		$('.js_btn_update').removeClass('is_hide');

		// formのアクション設定
		form = $('[name=shohins_toroku_form]');
		form.attr('action', getShohinKoshinUrl());

		$('#shohin_toroku_modal').modal();
	});
});