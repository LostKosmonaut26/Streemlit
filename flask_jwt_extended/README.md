Movile App

1.Доступ в браузер,вкл HTTP android:usesCleartextTraffic="true"

2.Созадать макет webView

3.Настройка webView

import android.webkit.WebSettings; import android.webkit.WebView; 
import android.webkit.WebViewClient; 
... 
private WebView webView; 
.... 
webView = findViewById(R.id.webview);
webView.setWebViewClient(new WebViewClient());

WebSettings webSettings = webView.getSettings();
webSettings.setJavaScriptEnabled(true);

webView.loadUrl("https://ваш-сайт.com");
