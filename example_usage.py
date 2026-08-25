from client import NeuralVoiceprintSpeakerDiarizationEngineClient

def main():
    client = NeuralVoiceprintSpeakerDiarizationEngineClient()
    res = client.diarize_speaker_voiceprints('https://assets.genpark.ai/audio/courtroom_deposition.wav', 5)
    print('Diarization Job: ' + res['diarization_job_id'] + ' (' + str(res['distinct_speakers_identified']) + ' speakers)')
    print('DER Error Rate: ' + str(res['diarization_error_rate_der_pct']) + '% | Overlap Resolution: ' + str(res['overlapping_speech_resolution_pct']) + '%')
    print('Speaker Turns: ' + str(res['speaker_turns_timeline_count']) + ' | RTTM File: ' + res['rttm_diarization_file_url'])

if __name__ == '__main__':
    main()
