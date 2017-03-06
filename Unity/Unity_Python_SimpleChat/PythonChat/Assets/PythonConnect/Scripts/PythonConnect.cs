using UnityEngine;
using UnityEngine.Events;
using System;
using System.Collections;
using System.IO;
using System.Net.Sockets;
using System.Threading;

public class PythonConnect : MonoBehaviour {

	[SerializeField] 	private string m_Host = "localhost";
	[SerializeField]	private int m_Port = 9999;
	[SerializeField]	private bool m_AutoConnect = false;

	public Action<string> OnReceiveMessage;

	private TcpClient m_Socket;
	private NetworkStream m_NetStream;

	private StreamReader m_StreamReader;
	private StreamWriter m_StreamWriter;

	private Thread m_ReceiveThread;

	private void Start() {
		if (m_AutoConnect) {
			Connect ();
		}
	}	

	private void Update() {
		
	}

	private void OnApplicationQuit() {
		CloseSocket ();
	}

	private void OnDestroy() {
		CloseSocket ();
	}

	public void Connect() {
		try {
			m_Socket = new TcpClient (m_Host, m_Port);
			m_NetStream = m_Socket.GetStream();
			m_StreamWriter = new StreamWriter (m_NetStream);
			m_StreamReader = new StreamReader (m_NetStream);
			StartCoroutine (CreateReceiveListener());
#if UNITY_EDITOR
			Debug.Log ("Connected host " + m_Host + " port " + m_Port);
#endif
		} catch (System.Exception ex) {
			Debug.Log (ex.Message);
		}
	}

	private IEnumerator CreateReceiveListener() {
		var waitingForEndOfFrame = new WaitForEndOfFrame ();
		while (true) {
			string receiveData = ReadSocket ();
			if (string.IsNullOrEmpty (receiveData) == false) {
				if (OnReceiveMessage != null) {
					OnReceiveMessage (receiveData);
				}
#if UNITY_EDITOR
				Debug.Log (receiveData);
#endif
			}
			yield return waitingForEndOfFrame;
		}
	}
		
	public void WriteSocket(string value) {
		if (m_StreamWriter == null)
			return;
//		var data = System.Text.Encoding.ASCII.GetBytes(value);
		m_StreamWriter.WriteLine (value);
		m_StreamWriter.Flush ();
	}

	public string ReadSocket() {
		var value = string.Empty;
		if (m_StreamReader == null)
			return value;
		if (m_NetStream.DataAvailable)
			value = m_StreamReader.ReadLine ();
		return value;
	}

	public void CloseSocket() {
		try {
			m_StreamReader.Close ();
			m_StreamWriter.Close ();
			m_NetStream.Close ();
		} catch (System.Exception ex) {
			Debug.Log (ex.Message);
		}
	}

}
