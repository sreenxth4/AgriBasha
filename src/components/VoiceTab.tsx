import { useState } from 'react'
import { speechToText, translate, textToSpeech } from '../lib/api'

const Recorder = ({ onStop }:{ onStop:(b:Blob)=>void }) => {
  const [rec, setRec] = useState<MediaRecorder|null>(null)
  const [recording, setRecording] = useState(false)
  const chunks: BlobPart[] = []
  const start = async () => {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true })
    const r = new MediaRecorder(stream, { mimeType: 'audio/webm' })
    r.ondataavailable = e => chunks.push(e.data)
    r.onstop = () => onStop(new Blob(chunks, { type: 'audio/webm' }))
    r.start(); setRec(r); setRecording(true)
  }
  const stop = () => { rec?.stop(); setRecording(false) }
  return <div>{!recording ? <button onClick={start}>Start</button> : <button onClick={stop}>Stop</button>}</div>
}

export default function VoiceTab(){
  const [sourceLang, setSourceLang] = useState('te')
  const [targetLang, setTargetLang] = useState('en')
  const [heard, setHeard] = useState(''); const [translated, setTranslated] = useState('')
  const [audioUrl, setAudioUrl] = useState<string|null>(null)

  const handleStop = async (blob: Blob) => {
    const stt = await speechToText(blob, sourceLang); setHeard(stt.text || '')
    const mt = await translate(stt.text || '', sourceLang, targetLang); setTranslated(mt.translatedText || '')
    const tts = await textToSpeech(mt.translatedText || '', targetLang);
    setAudioUrl(`data:${tts.mime};base64,${tts.audioBase64}`)
  }

  return (
    <div>
      <div style={{display:'flex', gap:8}}>
        <select value={sourceLang} onChange={e=>setSourceLang(e.target.value)}>
          <option value="te">Telugu</option><option value="hi">Hindi</option><option value="ta">Tamil</option><option value="en">English</option>
        </select>
        <select value={targetLang} onChange={e=>setTargetLang(e.target.value)}>
          <option value="en">English</option><option value="te">Telugu</option><option value="hi">Hindi</option><option value="ta">Tamil</option>
        </select>
      </div>
      <Recorder onStop={handleStop}/>
      <h3>Heard</h3><pre>{heard}</pre>
      <h3>Translated</h3><pre>{translated}</pre>
      {audioUrl && <audio controls src={audioUrl}></audio>}
    </div>
  )
}
