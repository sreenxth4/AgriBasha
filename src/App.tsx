import { useState } from 'react'
import VoiceTab from './components/VoiceTab'
import DocumentTab from './components/DocumentTab'
import TextTab from './components/TextTab'

export default function App(){
  const [tab, setTab] = useState<'voice'|'doc'|'text'>('voice')
  return (
    <div style={{maxWidth:900, margin:'0 auto', padding:16}}>
      <h1>AgriBasha</h1>
      <div style={{display:'flex', gap:8, marginBottom:12}}>
        <button onClick={()=>setTab('voice')}>Voice</button>
        <button onClick={()=>setTab('doc')}>Document</button>
        <button onClick={()=>setTab('text')}>Text</button>
      </div>
      {tab==='voice' && <VoiceTab/>}
      {tab==='doc' && <DocumentTab/>}
      {tab==='text' && <TextTab/>}
    </div>
  )
}
