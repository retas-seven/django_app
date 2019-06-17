$(document).ready(function() {
	// 画面の初期状態を設定
	init();
	// 登録／更新ボタン押下時の処理
	$(".js_execute_btn").on("click", execute);
});

/**
 * 画面初期化
 */
function init() {
	let form = $('[name=shohin_form]');

	if (mode == 'regist') {
		form.attr('action', shohin_regist_view_url);

	} else if (mode == 'update') {
		form.attr('action', shohin_update_view_url);
		// 型番は読み取りのみとし、更新させない
		$('#id_kataban').attr('readonly', true);
		// $('#id_kataban').addClass('form-control-plaintext');
	}
};

/**
 * 登録／更新ボタン押下時の処理
 */
function execute() {
	$('body').on('animsition.outEnd', () => {
		let form = $('[name=shohin_form]');
		form.submit();
	});
};

