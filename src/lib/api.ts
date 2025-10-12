import axios from 'axios'

const api = axios.create({ baseURL: import.meta.env.VITE_API_BASE || '/api' })

export async function speechToText(blob: Blob, lang='te'){
  const fd = new FormData(); fd.append('audio', blob); fd.append('lang', lang)
  const { data } = await api.post('/speech-to-text', fd)
  return data
}

export async function translate(text: string, source='te', target='en'){
  const { data } = await api.post('/translate', { text, source, target })
  return data
}

export async function textToSpeech(text: string, lang='te'){
  const { data } = await api.post('/text-to-speech', { text, lang })
  return data
}

export async function ocr(file: File, target?: string){
  const fd = new FormData(); fd.append('image', file); if (target) fd.append('target', target)
  const { data } = await api.post('/ocr', fd)
  return data
}

export default api
