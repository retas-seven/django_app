$(document).ready(function() {
	// ログインボタン押下時の処理
	$(".js_login_btn").on("click", execLogin);
});

/**
 * ログインボタン押下時の処理
 */
function execLogin() {
	$('body').on('animsition.outEnd', () => {
		$('#login_form').submit();
	});
}
