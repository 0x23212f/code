// Close the friggin' tab.

// "savedYourAss" variable (by closing tab) creation
// This variable is stored locally in Chrome sandbox
// as 'gorillaPwnWin'
chrome.tabs.onUpdated.addListener(function(tabId, changeInfo) {
    if (changeInfo.status === 'loading') {
    	if (changeInfo.url  === 'http://gorillavid.in/favicon.ico') {
    		chrome.tabs.remove(tabId);
    	}
    	if (changeInfo.url  === 'about:blank') {
    		chrome.tabs.remove(tabId);
    	}
        if (localStorage.gpwc === null) {
			localStorage.gpwc = '0';
		}
		if (parseInt(localStorage.gpwc) > 100) {
			var temp = parseInt(localStorage.gpwc/100);
			var temp = 100 * temp;
			var temp = localStorage.gpwc - temp;
			localStorage.gpwc = temp.toString();
		}
		chrome.browserAction.setBadgeBackgroundColor({ color: [96, 96, 96, 1] });
		var savedYA = parseInt(localStorage.gpwc);
		savedYA = savedYA + 1;
		localStorage.gpwc = savedYA.toString();
		chrome.browserAction.setBadgeText({text: savedYA.toString() });
    }
});