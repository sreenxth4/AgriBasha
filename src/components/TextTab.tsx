import { useState } from 'react'
import { translate, textToSpeech } from '../lib/api'

export default function TextTab(){
  const [source, setSource] = useState('en'); const [target, setTarget] = useState('te')
  const [input, setInput] = useState(''); const [out, setOut] = useState(''); const [audio, setAudio] = useState<string|null>(null)
  const go = async ()=>{ const r=await translate(input, source, target); setOut(r.translatedText||'') }
  const speak = async ()=>{ const r=await textToSpeech(out, target); setAudio(`data:${r.mime};base64,${r.audioBase64}`) }
  return (
    <div>
      <div style={{display:'flex', gap:8}}>
        <select value={source} onChange={e=>setSource(e.target.value)}>
          <option value="en">English</option><option value="te">Telugu</option><option value="hi">Hindi</option><option value="ta">Tamil</option>
        </select>
        <select value={target} onChange={e=>setTarget(e.target.value)}>
          <option value="te">Telugu</option><option value="hi">Hindi</option><option value="ta">Tamil</option><option value="en">English</option>
        </select>
      </div>
      <textarea rows={5} style={{width:'100%'}} value={input} onChange={e=>setInput(e.target.value)} placeholder="Paste weather/market/advisory text"/>
      <div style={{display:'flex', gap:8, marginTop:8}}>
        <button onClick={go}>Translate</button>
        <button onClick={speak} disabled={!out}>Speak</button>
      </div>
      <h3>Output</h3><pre>{out}</pre>
      {audio && <audio controls src={audio}></audio>}
    </div>
  )
}
