using UnityEngine;
using UnityEngine.Events;
using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using System.Net.Sockets;
using System.Threading;

public class PythonConnect : MonoBehaviour {

	[SerializeField] 	private string m_Host = "localhost";
	[SerializeField]	private int m_Port = 9999;
	[SerializeField]	private bool m_AutoConnect = false;

	public Action<string> OnReceiveMessage;

	private bool m_Connected;
	private TcpClient m_Socket;
	private NetworkStream m_NetStream;

	private StreamReader m_StreamReader;
	private StreamWriter m_StreamWriter;

	private Thread m_ReceiveThread;

	private List<string> m_ReceiveStrings;
	private int m_ReceiveStrCount;

	private void Awake() {
		m_ReceiveStrings = new List<string> ();
		m_ReceiveStrCount = m_ReceiveStrings.Count;
	}

	private void Start() {
		if (m_AutoConnect) {
			Connect ();
		}
	}	

	private void LateUpdate() {
		if (m_ReceiveStrCount != m_ReceiveStrings.Count) {
			if (OnReceiveMessage != null) {
				OnReceiveMessage (m_ReceiveStrings[m_ReceiveStrCount]);
				m_ReceiveStrCount = m_ReceiveStrings.Count;
			}
		}
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
			m_Connected = m_Socket.Connected;
			StartCoroutine (CreateReceiveListener());
#if UNITY_EDITOR
			Debug.Log ("Connected host " + m_Host + " port " + m_Port);
#endif
		} catch (System.Exception ex) {
			Debug.Log (ex.Message);
		}
	}

	private IEnumerator CreateReceiveListener() {
		m_ReceiveThread = new Thread (ReceiveListener);
		m_ReceiveThread.IsBackground = true;
		m_ReceiveThread.Start ();
		yield return null;
	}

	private void ReceiveListener() {
		while (m_Connected) {
			string receiveData = ReadSocket ();
			if (string.IsNullOrEmpty (receiveData) == false) {
				m_ReceiveStrings.Add (receiveData);
#if UNITY_EDITOR
				Debug.Log (receiveData);
#endif
			}
		}
	}
		
	public void WriteSocket(string value) {
		if (m_Connected == false)
			return;
		if (m_StreamWriter == null)
			return;
//		var data = System.Text.Encoding.ASCII.GetBytes(value);
		m_StreamWriter.WriteLine (value);
		m_StreamWriter.Flush ();
	}

	public string ReadSocket() {
		var value = string.Empty;
		if (m_Connected == false)
			return value;
		if (m_StreamReader == null)
			return value;
		if (m_NetStream.DataAvailable)
			value = m_StreamReader.ReadLine ();
		return value;
	}

	public void CloseSocket() {
		if (m_Connected == false)
			return;
		try {
			m_StreamReader.Close ();
			m_StreamWriter.Close ();
			m_NetStream.Close ();
		} catch (System.Exception ex) {
			Debug.Log (ex.Message);
		}
	}

}
