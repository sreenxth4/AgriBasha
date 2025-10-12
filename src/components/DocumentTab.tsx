import { useState } from 'react'
import { ocr } from '../lib/api'

export default function DocumentTab(){
  const [target, setTarget] = useState('te')
  const [extracted, setExtracted] = useState(''); const [translated, setTranslated] = useState('')
  const onFile = async (f: File) => {
    const res = await ocr(f, target); setExtracted(res.extractedText || ''); setTranslated(res.translatedText || '')
  }
  return (
    <div>
      <select value={target} onChange={e=>setTarget(e.target.value)}>
        <option value="te">Telugu</option><option value="hi">Hindi</option><option value="ta">Tamil</option><option value="en">English</option>
      </select>
      <input type="file" accept="image/*,application/pdf" onChange={e=>{const f=e.target.files?.[0]; if(f) onFile(f)}} />
      <h3>Extracted</h3><pre>{extracted}</pre>
      <h3>Translated</h3><pre>{translated}</pre>
    </div>
  )
}
