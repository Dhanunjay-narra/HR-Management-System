import React, { useState } from 'react';
import api from '../../services/api';
import { Bot, Send, X, Sparkles, BookOpen, AlertCircle, CheckCircle2 } from 'lucide-react';

interface AIAssistantChatModalProps {
  isOpen: boolean;
  onClose: () => void;
}

interface Message {
  role: 'user' | 'assistant';
  content: string;
  confidence?: number;
  citations?: Array<{ title: string; category: string; snippet: string }>;
  suggestedActions?: string[];
}

export const AIAssistantChatModal: React.FC<AIAssistantChatModalProps> = ({ isOpen, onClose }) => {
  const [query, setQuery] = useState('');
  const [loading, setLoading] = useState(false);
  const [messages, setMessages] = useState<Message[]>([
    {
      role: 'assistant',
      content: "Hello! I am your HR Management System AI Assistant. Ask me anything regarding company policies, leave entitlements, health insurance, remote work stipends, or HR workflows.",
      suggestedActions: [
        "What is our annual leave entitlement?",
        "How do remote work stipends work?",
        "How do I submit an expense reimbursement?"
      ]
    }
  ]);

  if (!isOpen) return null;

  const handleSend = async (textToSend?: string) => {
    const prompt = textToSend || query;
    if (!prompt.trim() || loading) return;

    const userMsg: Message = { role: 'user', content: prompt };
    setMessages((prev) => [...prev, userMsg]);
    setQuery('');
    setLoading(true);

    try {
      const res = await api.post('/ai/assistant/chat', { query: prompt, conversation_history: [] });
      const aiMsg: Message = {
        role: 'assistant',
        content: res.data.answer,
        confidence: res.data.confidence,
        citations: res.data.citations,
        suggestedActions: res.data.suggested_actions
      };
      setMessages((prev) => [...prev, aiMsg]);
    } catch (err: any) {
      setMessages((prev) => [
        ...prev,
        {
          role: 'assistant',
          content: 'Sorry, I encountered an issue connecting to the AI policy knowledge base. Please try again.'
        }
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/60 backdrop-blur-xs animate-in fade-in duration-200">
      <div className="bg-white rounded-2xl shadow-2xl w-full max-w-2xl flex flex-col h-[620px] overflow-hidden border border-slate-200">
        {/* Header */}
        <div className="px-6 py-4 bg-slate-900 text-white flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-9 h-9 rounded-xl bg-blue-600 flex items-center justify-center text-white shadow-md shadow-blue-500/30">
              <Bot className="w-5 h-5" />
            </div>
            <div>
              <h2 className="font-bold text-sm text-white flex items-center gap-1.5">
                HR Management System AI Knowledge Assistant
                <span className="px-2 py-0.5 rounded-full text-[10px] bg-blue-500/30 text-blue-300 font-semibold border border-blue-400/30">
                  RAG Grounded
                </span>
              </h2>
              <p className="text-[11px] text-slate-400">Semantic HR intelligence & policy search</p>
            </div>
          </div>
          <button
            onClick={onClose}
            className="p-1.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Message Thread */}
        <div className="flex-1 overflow-y-auto p-6 space-y-4 bg-slate-50">
          {messages.map((m, idx) => (
            <div key={idx} className={`flex ${m.role === 'user' ? 'justify-end' : 'justify-start'}`}>
              <div
                className={`max-w-[85%] rounded-2xl px-4 py-3 text-xs leading-relaxed ${
                  m.role === 'user'
                    ? 'bg-blue-600 text-white rounded-br-none shadow-sm'
                    : 'bg-white text-slate-800 border border-slate-200 rounded-bl-none shadow-sm'
                }`}
              >
                <div className="whitespace-pre-wrap">{m.content}</div>

                {/* Citations block */}
                {m.citations && m.citations.length > 0 && (
                  <div className="mt-3 pt-3 border-t border-slate-100 space-y-1.5">
                    <div className="text-[10px] font-semibold text-slate-400 uppercase tracking-wider flex items-center gap-1">
                      <BookOpen className="w-3 h-3 text-blue-500" />
                      Policy Citations ({Math.round((m.confidence || 0) * 100)}% Confidence)
                    </div>
                    {m.citations.map((c, cIdx) => (
                      <div key={cIdx} className="bg-slate-50 p-2 rounded-lg border border-slate-200/60 text-[11px] text-slate-600">
                        <span className="font-semibold text-blue-600">{c.title}</span>: {c.snippet}
                      </div>
                    ))}
                  </div>
                )}

                {/* Suggested actions chips */}
                {m.suggestedActions && m.suggestedActions.length > 0 && (
                  <div className="mt-3 flex flex-wrap gap-1.5">
                    {m.suggestedActions.map((s, sIdx) => (
                      <button
                        key={sIdx}
                        onClick={() => handleSend(s)}
                        className="px-2.5 py-1 rounded-full bg-blue-50 hover:bg-blue-100 text-blue-700 text-[10px] font-medium border border-blue-200 transition-colors"
                      >
                        {s}
                      </button>
                    ))}
                  </div>
                )}
              </div>
            </div>
          ))}

          {loading && (
            <div className="flex justify-start">
              <div className="bg-white border border-slate-200 rounded-2xl rounded-bl-none px-4 py-3 text-xs text-slate-500 flex items-center gap-2 shadow-xs">
                <Sparkles className="w-4 h-4 text-blue-600 animate-spin" />
                <span>Searching knowledge repository and generating answer...</span>
              </div>
            </div>
          )}
        </div>

        {/* Input Bar */}
        <div className="p-4 bg-white border-t border-slate-200">
          <form
            onSubmit={(e) => {
              e.preventDefault();
              handleSend();
            }}
            className="flex items-center gap-2"
          >
            <input
              type="text"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="Ask any policy, benefits, or HR question..."
              className="flex-1 bg-slate-50 border border-slate-200 rounded-xl px-4 py-2.5 text-xs text-slate-800 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-all"
            />
            <button
              type="submit"
              disabled={loading || !query.trim()}
              className="px-4 py-2.5 rounded-xl bg-blue-600 hover:bg-blue-700 disabled:opacity-50 text-white text-xs font-semibold flex items-center gap-1.5 shadow-sm transition-colors"
            >
              <Send className="w-3.5 h-3.5" />
              <span>Ask</span>
            </button>
          </form>
        </div>
      </div>
    </div>
  );
};
