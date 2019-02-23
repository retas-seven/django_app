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

	// モーダルを開くか判別
	if ($('.js_open_regist_shohin_modal').val() == "True") {
		$('#regist_shohin_modal').modal();
	}
	if ($('.js_open_update_shohin_modal').val() == "True") {
		$('#update_shohin_modal').modal();
	}

	/**
	 * 削除ボタン押下時の処理
	 */
    $('.js_delete_btn').click(function(e) {
        if(!confirm('削除しますか？')){
            return false;
        }
		
		kataban = $(this).parents('td').data('kataban');
		form = $('[name=shohin_sakujo_form]');
		$('.js_shohin_sakujo_key_kataban').val(kataban);
		form.submit();
	});
	
	/**
	 * ダイアログ（登録）表示ボタン押下時の処理
	 */
    $('.js_regist_btn').click(function(e) {
		// $('#id_kataban').val('');
		// $('#id_shohinName').val('');
		// $('#id_price').val('');
		// $('#id_zaikosu').val('');
		// $('#id_memo').val('');
		
		// $('#id_kataban').attr('readonly', false);
		// $('#id_kataban').removeClass('form-control-plaintext');

		// 更新、登録ボタンの表示切り替え
		// $('.js_btn_update').addClass('is_hide');
		// $('.js_btn_regist').removeClass('is_hide');

		// formのアクション設定
		// form = $('[name=shohins_toroku_form]');
		// form.attr('action', getShohinTorokuUrl());

		$('#regist_shohin_modal').modal();
	});
	
	/**
	 * ダイアログ（更新）表示ボタン押下時の処理
	 */
    $('.js_update_btn').click(function(e) {
		let datas = $(this).parents('td');

		$('#id_updateKataban').val(datas.data('kataban'));
		$('#id_updateShohinName').val(datas.data('shohin_name'));
		$('#id_updatePrice').val(datas.data('price'));
		$('#id_updateZaikosu').val(datas.data('zaikosu'));
		$('#id_updateMemo').val(datas.data('memo'));
		
		// 型番は読み取りのみとし、更新させない
		$('#id_updateKataban').attr('readonly', true);
		$('#id_updateKataban').addClass('form-control-plaintext');

		// 更新、登録ボタンの表示切り替え
		// $('.js_btn_regist').addClass('is_hide');
		// $('.js_btn_update').removeClass('is_hide');

		// formのアクション設定
		// form = $('[name=shohins_toroku_form]');
		// form.attr('action', getShohinKoshinUrl());

		$('#update_shohin_modal').modal();
	});
});