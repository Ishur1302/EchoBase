def handle_barge_in(is_user_speaking, tts_player):
    if is_user_speaking and tts_player.is_playing:
        tts_player.stop()
        print("Barge-in detected: Muting AI output.")
