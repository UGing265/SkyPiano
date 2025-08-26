import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.tsx'
import TestPage from './pages/TestPage.tsx'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
   <TestPage />
  </StrictMode>,
)
