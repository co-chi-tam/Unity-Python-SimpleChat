using UnityEngine;
using UnityEngine.UI;
using System.Collections;

public class ChatController : MonoBehaviour {

	[SerializeField]	private PythonConnect m_PythonConnect;
	[SerializeField]	private Text m_MessageBoard;

	void Start() {
		m_PythonConnect.OnReceiveMessage += OnClientRecevieMessage;
	}

	private void OnClientRecevieMessage(string value) {
		m_MessageBoard.text += "\n" + value;
	}

	public void SubmitText(InputField value) {
		var chatValue = value.text;
		if (string.IsNullOrEmpty (chatValue))
			return;
		m_PythonConnect.WriteSocket (chatValue);
		value.text = string.Empty;
	}

}
