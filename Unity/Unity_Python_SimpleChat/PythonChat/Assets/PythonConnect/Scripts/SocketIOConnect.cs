using UnityEngine;
using System.Collections;
using System.Collections.Generic;
using SocketIO;
using System.Threading;

public class SocketIOConnect : MonoBehaviour {

	[SerializeField]	private SocketIOComponent m_SocketIO;

	private void Start() {
		m_SocketIO.autoConnect = false;
		m_SocketIO.Connect ();
		var data = new JSONObject ();
		data.AddField ("aaa", "bbb");
		m_SocketIO.On ("message", (evnt) => {
			Debug.Log (evnt.data.ToString());
		});
		m_SocketIO.Emit ("message", data);
	}

	private void Awake() {
		var t = new Thread (new ThreadStart (() => {
			// TODO 
			Thread.Sleep (1000);
			// TODO

		}));
		t.IsBackground = true;
		t.Start ();
	}



}
