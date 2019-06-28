$(document).ready(function() {
	// 新規登録ボタン押下時の処理
	$(".js_signup_btn").on("click", execSignup);
});

/**
 * 新規登録ボタン押下時の処理
 */
function execSignup() {
	$('body').on('animsition.outEnd', () => {
		$('#signup_form').submit();
	});
}
