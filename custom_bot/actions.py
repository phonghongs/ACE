#!/usr/bin/env python3
"""
Custom actions for the speech-to-speech bot.

This file contains custom actions that can be used in Colang flows, including:
- Spurious transcript filtering
- Custom API calls
- Other utility functions
"""

import logging
from nemoguardrails.actions.actions import action

logger = logging.getLogger("custom_actions")

# Transcript filtering for spurious transcript and filler words
FILTER_WORDS = [
    "yeah",
    "okay",
    "right",
    "yes",
    "yum",
    "and",
    "one",
    "all",
    "when",
    "thank",
    "but",
    "next",
    "what",
    "i see",
    "the",
    "hmm",
    "mmm",
    "so that",
    "why",
    "that",
    "well",
]

INCLUDE_WORDS = ["hi", "hello"]

@action(name="IsSpuriousAction")
async def is_spurious(query):
    """
    Filter transcript less than 3 chars or in FILTER_WORDS list to avoid spurious transcript and filler words.
    """
    if query.strip().lower() in FILTER_WORDS or (len(query) < 3 and query.strip().lower() not in INCLUDE_WORDS):
        return True
    else:
        return False

@action(name="LogTranscriptAction")
async def log_transcript(transcript, is_final=True):
    """
    Log the transcript for debugging purposes.
    """
    logger.info(f"{'Final' if is_final else 'Interim'} transcript: {transcript}")
    return True
